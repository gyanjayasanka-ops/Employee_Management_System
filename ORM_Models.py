from sqlalchemy import Column, Integer, String, Float

from database import base

class Employee(base):

    __tablename__ = "employees"

    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String(100),nullable=False)
    last_name = Column(String(100),nullable=False)
    email= Column(String(150), unique=True,nullable=False,index=True)
    department = Column(String(100),nullable=False)
    salary = Column(Float, nullable=False)
    role = Column(String, nullable=False)

