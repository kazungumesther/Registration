from pydantic import BaseModel


class CourseBase(BaseModel):
   title: str
   code: str
   credits: int
   semester: str
   teacher_id: int


class CourseCreate(CourseBase):
   pass


class CourseResponse(CourseBase):
   id: int


   class Config:
       from_attributes = True
