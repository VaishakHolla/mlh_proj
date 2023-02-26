from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Agency(Base):
    __tablename__ = 'agency'
    id = Column(Integer, primary_key=True)
    agency_name = Column(String)
    agency_url = Column(String)
    agency_timezone = Column(String)
    agency_lang = Column(String)
    agency_phone = Column(String)
    agency_fare_url = Column(String)

class Calendar(Base):
    __tablename__ = 'calendar'
    id = Column(Integer, primary_key=True)
    service_id = Column(String)
    monday = Column(Integer)
    tuesday = Column(Integer)
    wednesday = Column(Integer)
    thursday = Column(Integer)
    friday = Column(Integer)
    saturday = Column(Integer)
    sunday = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)

class CalendarDate(Base):
    __tablename__ = 'calendar_date'
    id = Column(Integer, primary_key=True)
    service_id = Column(String)
    date = Column(Date)
    exception_type = Column(Integer)

class FeedInfo(Base):
    __tablename__ = 'feed_info'
    id = Column(Integer, primary_key=True)
    feed_publisher_name = Column(String)
    feed_publisher_url = Column(String)
    feed_lang = Column(String)
    feed_start_date = Column(Date)
    feed_end_date = Column(Date)
    feed_version = Column(String)

class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True)
    route_id = Column(String)
    agency_id = Column(String)
    route_short_name = Column(String)
    route_long_name = Column(String)
    route_desc = Column(String)
    route_type = Column(Integer)
    route_url = Column(String)
    route_color = Column(String)
    route_text_color = Column(String)

class Shape(Base):
    __tablename__ = 'shapes'
    id = Column(Integer, primary_key=True)
    shape_id = Column(String)
    shape_pt_lat = Column(Float)
    shape_pt_lon = Column(Float)
    shape_pt_sequence = Column(Integer)
    shape_dist_traveled = Column(Float)

class Stop(Base):
    __tablename__ = 'stops'
    id = Column(Integer, primary_key=True)
    stop_id = Column(String)
    stop_code = Column(String)
    stop_name = Column(String)
    stop_desc = Column(String)
    stop_lat = Column(Float)
    stop_lon = Column(Float)
    zone_id = Column(String)
    stop_url = Column(String)
    location_type = Column(Integer)
    parent_station = Column(String)

class StopTime(Base):
    __tablename__ = 'stop_times'
    id = Column(Integer, primary_key=True)
    trip_id = Column(String)
    arrival_time = Column(String)
    departure_time = Column(String)
    stop_id = Column(String)
    stop_sequence = Column(Integer)
    stop_headsign = Column(String)
    pickup_type = Column(Integer)
    drop_off_type = Column(Integer)
    shape_dist_traveled = Column(Float)

class Trip(Base):
    __tablename__ = 'trips'
    id = Column(Integer, primary_key=True)
    route_id = Column(String)
    service_id = Column(String)
    trip_id = Column(String)
    trip_headsign = Column(String)
    trip_short_name = Column(String)
    direction_id = Column(Integer)
    block_id = Column(String)
    shape_id = Column(String)
