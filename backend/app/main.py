from fastapi import FastAPI,APIRouter


app = FastAPI(title="tdt api",openapi_url="/openapi.json")

api_router=APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, World!"}


app.include_router(api_router)