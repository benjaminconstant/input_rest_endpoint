from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "items"

    pageId = Column(Integer, primary_key=True, index=True)
    correlationId = Column(String, index=True)
    src = Column(String, index=True)