from fastapi import FastAPI,APIRouter

from fastapi.middleware.cors import CORSMiddleware

from app.api import deps
from app.api.api_v1.api import api_router

from app.core.config import settings
app = FastAPI(title="tdt api",openapi_url="/openapi.json")

root_router=APIRouter()

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        # allow_origin_regex=settings.BACKEND_CORS_ORIGIN_REGEX,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )




@root_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, World!"}


app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)