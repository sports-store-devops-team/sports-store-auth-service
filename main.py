import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import users_collection
from observability import configure_observability
from routes import auth

logger = logging.getLogger("auth-service")

app = FastAPI(title="Sports Store — Auth Service")
configure_observability(app, "auth-service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api")


@app.on_event("startup")
async def create_indexes():
    try:
        await users_collection.create_index("email", unique=True)
    except Exception:  # Mongo may be unavailable (e.g. unit tests)
        logger.warning(
            "database_index_creation_skipped",
            extra={"event": "database_index_creation_skipped"},
        )


@app.get("/health")
def health():
    return {"status": "ok", "service": "auth-service"}
