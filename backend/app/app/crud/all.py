from typing import Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.all import Agency,Calendar,CalendarDate,Trip,Shape,Stop,StopTime,Route,FeedInfo
from app.schemas.all import AgencyBase,AgencyCreate,AgencyUpdate,FeedInfoBase,FeedInfoCreate,FeedInfoUpdate,CalendarBase,CalendarCreate,CalendarUpdate,ShapeBase,ShapeCreate,ShapeUpdate,StopBase,StopCreate,StopUpdate,StopTimeUpdate,StopTimeBase,StopTimeCreate,RouteBase,RouteCreate,RouteUpdate,TripBase,TripCreate,TripUpdate,CalendarDateBase,CalendarDateCreate,CalendarDateUpdate

class CRUDAgency(CRUDBase[Agency,AgencyCreate,AgencyUpdate]):
    pass
agency=CRUDAgency(Agency)

class CRUDTrip(CRUDBase[Trip,TripCreate,TripUpdate]):
    pass
trip=CRUDTrip(Trip)

class CRUDCalendar(CRUDBase[Calendar,CalendarCreate,CalendarUpdate]):
    pass
calendar=CRUDCalendar(Calendar)

class CRUDCalendarDate(CRUDBase[CalendarDate,CalendarDateCreate,CalendarDateUpdate]):
    pass
calendar_date=CRUDCalendarDate(CalendarDate)

class CRUDRoute(CRUDBase[Route,RouteCreate,RouteUpdate]):
    pass
route=CRUDRoute(Route)

class CRUDFeedInfo(CRUDBase[FeedInfo,FeedInfoCreate,FeedInfoUpdate]):
    pass
feed_info = CRUDFeedInfo(FeedInfo)

class CRUDShape(CRUDBase[Shape,ShapeCreate,ShapeUpdate]):
    pass
shape = CRUDShape(Shape)

class CRUDStop(CRUDBase[Stop,StopCreate,StopUpdate]):
    pass
stop = CRUDStop(Stop)

class CRUDStopTime(CRUDBase[StopTime,StopTimeCreate,StopTimeUpdate]):
    pass
stop_time = CRUDStopTime(StopTime)