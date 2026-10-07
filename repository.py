from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import EmployeeCreate, EmployeeResponse


class EmployeeRepository:

    async def create_employee(self, session: AsyncSession, employee: EmployeeCreate):

        new_employee= EmployeeResponse(
            first_name=employee.first_name,
            last_name=employee.last_name,
            email=employee.email,
            department=employee.departmen,
            role=employee.role,
            salary=employee.salary
        )

        session.add(new_employee)
        await session.flush()
        return new_employee

    async  def get_by_email(self, db:AsyncSession, email:str):
        result = await db.execute(select(EmployeeResponse).where(EmployeeResponse.email == email))

        return result.scalar_one_or_none()