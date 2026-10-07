from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from models import EmployeeCreate
from repository import EmployeeRepository


class EmployeeServicee:

    def __init__(self):
        self.repository = EmployeeRepository()

    async def create_employee(self,db:AsyncSession, employee:EmployeeCreate):

        #cheeck dduplicate email
        existing_employee = await self.repository.get_by_email(db,employee.email)

        if existing_employee:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Email already exists")

        return await self.repository.create_employee(db,employee)