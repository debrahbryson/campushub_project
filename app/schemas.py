from pydantic import BaseModel

class UserCreate(BaseModel):
	student_id: str
	password: str

class UserLogin(BaseModel):
	student_id: str
	password: str

class PostCreate(BaseModel):
	content: str

class CommentCreate(BaseModel):
	text: str
