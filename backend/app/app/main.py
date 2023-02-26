from fastapi import FastAPI,APIRouter

import json,decimal, datetime
from sqlalchemy import create_engine, MetaData, Table

from fastapi.middleware.cors import CORSMiddleware

from app.api import deps
from app.api.api_v1.api import api_router

from app.core.config import settings
app = FastAPI(title="tdt api",openapi_url="/openapi.json")

root_router=APIRouter()
engine = create_engine('postgresql://admin_new:root@localhost:5432/test_new')
metadata = MetaData()

table_name = Table('trips', metadata,schema='gtfs')
metadata.reflect(bind=engine, schema='gtfs')

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        # allow_origin_regex=settings.BACKEND_CORS_ORIGIN_REGEX,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)

@app.get("/table")
async def read_table():
    with engine.connect() as conn:
        result = conn.execute(table_name.select())
        print(f"Rows returned: {result.rowcount}")
        rows = result.fetchall()
        # for row in rows:
        #     print(row)
        return json.dumps([dict(r) for r in rows], default=alchemyencoder)
        # return rows

@root_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, World!"}


app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)