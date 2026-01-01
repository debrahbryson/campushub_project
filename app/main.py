from fastapi import FastAPI, Depends, WebSocket
from sqlalchemy.orm import Session
from database import Base, engine
from models import User, Post, Comment, Like
from schemas import *
from auth import hash_password, verify_password, create_access_token
from deps import get_db, get_current_user
from websocket import chat

app = FastAPI(title="CampusHub")
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "API is running"}


@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
	u = User(student_id=user.student_id, password=hash_password(user.password))
	db.add(u)
	db.commit()
	return {"message": "registered"}

@app.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
	user = db.query(User).filter(User.student_id == data.student_id).first()
	if not user or not verify_password(data.password, user.password):
		return {"error": "invalid credentials"}
	token = create_access_token({"sub": user.student_id})
	return {"access_token": token}

@app.post("/posts")
def create_post(post: PostCreate, user=Depends(get_current_user),
	db=Depends(get_db)):
		p = Post(content=post.content, owner_id=user.id)
		db.add(p)
		db.commit()
		return {"message": "post created"}

@app.get("/posts")
def get_posts(db=Depends(get_db)):
	return db.query(Post).all()

@app.post("/like/{post_id}")
def like(post_id: int, user=Depends(get_current_user), db=Depends(get_db)):
	db.add(Like(post_id=post_id, user_id=user.id))
	db.commit()
	return {"message": "liked"}

@app.post("/comment/{post_id}")
def comment(post_id: int, c: CommentCreate, user=Depends(get_current_user),
	db=Depends(get_db)):
		db.add(Comment(text=c.text, post_id=post_id))
		db.commit()
		return {"message": "commented"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
	await chat(ws)
