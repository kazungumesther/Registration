from pydantic import BaseModel, EmailStr


class TeacherBase(BaseModel):
   name: str
   email: EmailStr
   department: str
   phone: str
   employee_number: int


class TeacherCreate(TeacherBase):
   pass


class TeacherResponse(TeacherBase):
   id: int


   class Config:
       from_attributes = True



