import json
from huey import SqliteHuey
from functools import wraps
from .config import settings
from .database import SessionLocal
from .models.dlq import DeadLetter

huey = SqliteHuey(filename=settings.HUEY_DB_URL)


def send_to_dlq(task_data, error):
    db = SessionLocal()
    try:
        payload_str = json.dumps(
            {"args": task_data.get("args", []), "kwargs": task_data.get("kwargs", {})}, default=str
        )
        dlq_entry = DeadLetter(
            task_name=task_data.get("func", "unknown_task"),
            payload=payload_str,
            error_message=str(error),
        )
        db.add(dlq_entry)
        db.commit()
        print(f"[DLQ] Task {dlq_entry.task_name} persisted to database DLQ.")
    except Exception as e:
        print(f"[DLQ-CRITICAL] Failed to write to DLQ database: {e}")
    finally:
        db.close()


def with_dlq(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            send_to_dlq({"func": func.__name__, "args": args, "kwargs": kwargs}, e)
            raise e

    return wrapper
