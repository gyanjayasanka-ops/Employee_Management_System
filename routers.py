from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database import get_session
from models import EmployeeCreate, EmployeeResponse
from service import EmployeeServicee

router = APIRouter(prefix="/employees",tags=["Employees"])

employee_servicee = EmployeeServicee()

@router.post("/",response_model=EmployeeResponse,status_code=status.HTTP_201_CREATED)
async def create_employee(employee:EmployeeCreate,db:AsyncSession=Depends(get_session)):
    return await employee_servicee.create_employee(db, employee)