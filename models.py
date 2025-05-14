from sqlalchemy import Column, Integer, String
#from geoalchemy2 import Geometry
from db_config import ORMBaseModel
from pydantic import BaseModel

# TODO Wzorując się na poniższych przykładach, zdefiniuj odpowienie modele w swojej aplikacji. TUTAJ ZROBIC SWOJA 

# class Person(ORMBaseModel):
#     __tablename__ = 'person'
#     id = Column(Integer, primary_key=True, index=True)
#     first_name = Column(String, nullable=False)
#     last_name = Column(String, nullable=False)
#     person_type_id = Column(Integer, index=True, nullable=False)
#     #position = Column(Geometry(geometry_type='POINT', srid=2180))

# class PersonCreate(BaseModel):
#     first_name: str
#     last_name: str
#     person_type_id: int
#     #position: str  # format WKT, np. "POINT(123 456)"

# class PositionUpdate(BaseModel):
#     #position: str  # format WKT

class Room(ORMBaseModel):
    __tablename__='room'
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String,nullable=False)
    room_category_id = Column(Integer, index=True, nullable=False)
    floor_id = Column(Integer, index=True, nullable=False)

class RoomCreate(BaseModel):
    number: str
    room_category_id: int
    floor_id: int

class FloorUpdate(BaseModel):
    floor_id: int