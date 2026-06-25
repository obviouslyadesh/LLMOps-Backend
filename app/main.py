from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.chat import router as chat_router
from app.api.routes.health import router as health_router
from app.api.routes.search import router as search_router
from app.api.routes.upload import router as upload_router
from app.core.config import settings
from app.core.middleware import APIKeyMiddleware, RequestTimingMiddleware

app = FastAPI(title=settings.APP_NAME, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(APIKeyMiddleware)
app.add_middleware(RequestTimingMiddleware)

app.include_router(health_router)
app.include_router(upload_router)
app.include_router(search_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {"message": "LLMOps Platform Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
