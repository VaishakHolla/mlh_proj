from typing import Optional, List
from pydantic import BaseModel, validator


class AgencyBase(BaseModel):
    agency_id: str
    agency_name: str
    agency_url: str
    agency_timezone: str
    agency_lang: Optional[str]

    @validator('agency_id')
    def agency_id_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v
class AgencyCreate(AgencyBase):
    pass

class AgencyUpdate(AgencyBase):
    pass

class CalendarDateBase(BaseModel):
    service_id: str
    date: str
    exception_type: int

class CalendarDateCreate(CalendarDateBase):
    pass

class CalendarDateUpdate(CalendarDateBase):
    pass

class CalendarBase(BaseModel):
    service_id: str
    monday: int
    tuesday: int
    wednesday: int
    thursday: int
    friday: int
    saturday: int
    sunday: int
    start_date: str
    end_date: str

class CalendarCreate(CalendarBase):
    pass

class CalendarUpdate(CalendarBase):
    pass

class FeedInfoBase(BaseModel):
    feed_publisher_name: str
    feed_publisher_url: str
    feed_lang: Optional[str]
    feed_start_date: Optional[str]
    feed_end_date: Optional[str]

class FeedInfoCreate(FeedInfoBase):
    pass

class FeedInfoUpdate(FeedInfoBase):
    pass

class RouteBase(BaseModel):
    route_id: str
    agency_id: Optional[str]
    route_short_name: str
    route_long_name: str
    route_type: int
    route_color: Optional[str]
    route_text_color: Optional[str]

    @validator('route_id')
    def route_id_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

class RouteCreate(RouteBase):
    pass

class RouteUpdate(RouteBase):
    pass

class ShapeBase(BaseModel):
    shape_id: str
    shape_pt_lat: float
    shape_pt_lon: float
    shape_pt_sequence: int

class ShapeCreate(ShapeBase):
    pass

class ShapeUpdate(ShapeBase):
    pass

class StopTimeBase(BaseModel):
    trip_id: str
    arrival_time: str
    departure_time: str
    stop_id: str
    stop_sequence: int

class StopTimeCreate(StopTimeBase):
    pass

class StopTimeUpdate(StopTimeBase):
    pass

class StopBase(BaseModel):
    stop_id: str
    stop_name: str
    stop_lat: float
    stop_lon: float
    stop_code: Optional[str]
    stop_desc: Optional[str]
    zone_id: Optional[str]
    location_type: Optional[int]
    parent_station: Optional[str]

    @validator('stop_id')
    def stop_id_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

class StopCreate(StopBase):
    pass

class StopUpdate(StopBase):
    pass

class TripBase(BaseModel):
    route_id: str
    service_id: str
    trip_id: str
    trip_headsign: Optional[str]
    direction_id: Optional[int]
    shape_id: Optional[str]
    wheelchair_accessible: Optional[int]
    bikes_allowed: Optional[int]

class TripCreate(TripBase):
    pass

class TripUpdate(TripBase):
    pass