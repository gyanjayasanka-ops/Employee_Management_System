from typing import Optional

from pydantic import BaseModel, Field, EmailStr, ConfigDict


class EmployeeCreate(BaseModel):
    first_name: str = Field(...,min_length=2, max_length=100)
    last_name: str = Field(..., min_length=2,max_length=100)
    email: str = Field(...,min_length=2,max_length=100)
    department: str = Field(...,min_length=2,max_length=100)
    salary:float = Field(..., gt=0)
    role: str = Field(...,min_length=2,max_length=50)

class EmployeePatch(BaseModel):
    first_name: Optional[str] = Field(None,min_length=2, max_length=100)
    last_name: Optional[str] = Field(..., min_length=2,max_length=100)
    email: Optional[str] = Field(...,min_length=2,max_length=100)
    department: Optional[str]= Field(...,min_length=2,max_length=100)
    salary:Optional[float]= Field(..., gt=0)
    role: Optional[str] = Field(..., min_length=2, max_length=50)

class EmployeeResponse(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str
    department:str
    salary:float
    role:str

    model_config = ConfigDict(from_attributes=True)