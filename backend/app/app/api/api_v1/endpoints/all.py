import asyncio
from typing import Any, Optional

import httpx
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud
from app.api import deps

from app.schemas.all import (AgencyBase,AgencyCreate,AgencyUpdate,FeedInfoBase,FeedInfoCreate,FeedInfoUpdate,CalendarBase,CalendarCreate,CalendarUpdate,ShapeBase,ShapeCreate,ShapeUpdate,StopBase,StopCreate,StopUpdate,StopTimeUpdate,StopTimeBase,StopTimeCreate,RouteBase,RouteCreate,RouteUpdate,TripBase,TripCreate,TripUpdate,CalendarDateBase,CalendarDateCreate,CalendarDateUpdate)
from app.models.all import (Agency,Trip,Route,StopTime,Shape,Stop,Calendar,CalendarDate,FeedInfo)
from sqlalchemy import create_engine,text

# Replace USERNAME, PASSWORD, HOST, PORT, DATABASE, and SCHEMA with your own values
# engine = create_engine('postgresql://admin_new:root@localhost:5432/test_new')

# sql_query = text('SELECT * FROM gtfs.routes WHERE id = :id',{'id': 1})
# params = {'id': 1}
# with engine.connect() as conn:
#     result = conn.execute(('SELECT * FROM gtfs.routes WHERE id = :id',{'id': '1'}))
#     for row in result:
#         print(row)

router = APIRouter()

@router.get("/{route_id}",status_code=200, response_model=AgencyBase)
def fetch_route(*,route_id:int,db: Session = Depends(deps.get_db))->Any:
    
    result=crud.route.get(db=db,id=route_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Recipe with ID {recipe_id} not found"
        )

    return result