rom pydantic import BaseModel, EmailStr


class StudentBase(BaseModel):
   name: str
   age: int
   email: EmailStr
   country: str
   idnumber: int


class StudentCreate(StudentBase):
   pass


class StudentResponse(StudentBase):
   id: int


   class Config:
       from_attributes = True
