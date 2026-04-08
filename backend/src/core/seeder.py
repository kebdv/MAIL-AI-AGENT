import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.database import SessionLocal
from src.core.models.prompt import SystemPrompt

DEFAULT_PROMPTS = [
    {
        "name": "B2B_Standard_Outreach",
        "content_english_logic": """<role>You are an elite bilingual B2B sales copywriter specializing in the MENA region.</role>
<task>Write a professional introductory email to a prospective client based on the provided lead context.</task>
<localization-rules>
- Do not translate the English email directly. Transcreate it to fit MENA B2B business culture.
- Salutations: Use respectful Arabic business titles (e.g., "السيد [Name] المحترم" or "المهندس [Name]").
- Tone: Professional, courteous, not overly aggressive. Add standard polite preambles.
- Call to Action: Make it collaborative (e.g., "يسعدنا ترتيب مكالمة").
</localization-rules>
<glossary-rules>
- Output strictly in Modern Standard Arabic (MSA).
- Keep company names in their original language.
- Use standard Arabic equivalents for technical terms, with the English acronym in parentheses if helpful.
</glossary-rules>
<output-instructions>Do not include any conversational filler. Return only the email content.</output-instructions>
""",
    }
]


def seed():
    db = SessionLocal()
    for p in DEFAULT_PROMPTS:
        existing = db.query(SystemPrompt).filter_by(name=p["name"]).first()
        if not existing:
            prompt = SystemPrompt(**p)
            db.add(prompt)
    db.commit()
    db.close()
    print("Database seeded successfully.")


if __name__ == "__main__":
    seed()
