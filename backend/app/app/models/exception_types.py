from sqlalchemy import Column, Integer, String
from app.db.base_class import Base

class ExceptionType(Base):
    __tablename__ = 'exception_types'

    exception_type = Column(Integer, primary_key=True)
    description = Column(String)