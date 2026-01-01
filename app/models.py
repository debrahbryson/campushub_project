from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	student_id = Column(String, unique=True, index=True)
	password = Column(String)

	posts = relationship("Post", back_populates="owner")

class Post(Base):
	__tablename__ = "posts"
	id = Column(Integer, primary_key=True)
	content = Column(Text)
	owner_id = Column(Integer, ForeignKey("users.id"))

	owner = relationship("User", back_populates="posts")
	comments = relationship("Comment", back_populates="post")

class Comment(Base):
	__tablename__ = "comments"
	id = Column(Integer, primary_key=True)
	text = Column(Text)
	post_id = Column(Integer, ForeignKey("posts.id"))

	post = relationship("Post", back_populates="comments")

class Like(Base):

	__tablename__ = "likes"
	id = Column(Integer, primary_key=True)
	post_id = Column(Integer)
	user_id = Column(Integer)
