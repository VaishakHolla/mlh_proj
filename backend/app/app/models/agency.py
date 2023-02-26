from sqlalchemy import Column, Integer, String, ForeignKey,Text
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Agency(Base):
    __tablename__ = 'agency'
    feed_index = Column(Integer, primary_key=True)
    agency_id = Column(Text, default='')
    agency_name = Column(Text, nullable=False)
    agency_url = Column(Text, nullable=False)
    agency_timezone = Column(Text, nullable=False)
    agency_lang = Column(Text)
    agency_phone = Column(Text)
    agency_fare_url = Column(Text)
    agency_email = Column(Text)
    bikes_policy_url = Column(Text)
    feed_info = relationship("FeedInfo", back_populates="agencies")