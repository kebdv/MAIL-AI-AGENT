from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.modules.ingestion.router import router as ingestion_router
from src.modules.enrichment.router import router as enrichment_router
from src.modules.generation.router import router as generation_router
from src.modules.delivery.router import router as delivery_router

app = FastAPI(title="MAIL AI AGENT API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingestion_router, prefix="/api/v1/ingest", tags=["Ingestion"])
app.include_router(enrichment_router, prefix="/api/v1/enrich", tags=["Enrichment"])
app.include_router(generation_router, prefix="/api/v1/generate", tags=["Generation"])
app.include_router(delivery_router, prefix="/api/v1/delivery", tags=["Delivery"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
