from fastapi import APIRouter
from  app.api.api_v1.endpoints import all
api_router=APIRouter()

api_router.include_router(all.router,prefix="/all",tags=["all"])
