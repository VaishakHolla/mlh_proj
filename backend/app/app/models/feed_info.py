# from sqlalchemy import Column, Integer, String, Date, UniqueConstraint
# from sqlalchemy.ext.declarative import declarative_base

# from app.db.base_class import Base

# class FeedInfo(Base):
#     __tablename__ = 'feed_info'

#     feed_index = Column(Integer, primary_key=True, autoincrement=True)
#     feed_publisher_name = Column(String, nullable=False)
#     feed_publisher_url = Column(String, nullable=False)
#     feed_lang = Column(String, nullable=False)
#     default_lang = Column(String, default=None)
#     feed_start_date = Column(Date, default=None)
#     feed_end_date = Column(Date, default=None)
#     feed_version = Column(String, default=None)
#     feed_download_date = Column(Date, nullable=True)
#     feed_file = Column(String, nullable=False, unique=True)
#     feed_timezone = Column(String, default=None)
#     feed_id = Column(String, default=None)
#     feed_contact_url = Column(String, default=None)
#     feed_contact_email = Column(String, default=None)

#     __table_args__ = (
#         UniqueConstraint('feed_file', name='feed_file_uniq'),
#     )
