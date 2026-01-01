# CampusHub Project

## Description
CampusHub is a small hangout spot for a university. Students and teachers can chat, post, comment, like, and share ideas. The goal is to create a simple social platform for everyone on campus to connect and interact.

## Features
- Post section  
- Comment on posts  
- Like posts  
- Register / Login  
- Real-time chat  

## How to Run
Make sure you have **FastAPI** and **Uvicorn** installed. Then run:

```bash
uvicorn main:app --reload
```

## Tools and Why I Chose Them
- FastAPI:
I chose FastAPI because it is modern, fast, and easy to learn. It allows me to build APIs quickly with minimal code, while still supporting features like data validation and dependency injection.
It also supports asynchronous programming, which is helpful when multiple users interact with the app at the same time.

- WebSockets:
I used WebSockets to implement real-time chat. Unlike normal HTTP requests, WebSockets keep a constant connection open between the client and server.
This means messages appear instantly to all users without refreshing, making the chat experience smooth and interactive.

- Session:
Sessions are used to keep users logged in across different pages and actions. 
Without sessions, users would need to re-login every time they move between posts, comments, or chat, which would be annoying.
Sessions also help keep track of user identity safely on the server side.

- Depends:
FastAPI's Depends is used for dependency injection. 
It helps me reuse code like authentication checks, database connections, and other repeated logic.
This keeps the code cleaner and easier to maintain, instead of writing the same logic in every route.

- SQLAlchemy:
I chose SQLAlchemy as the ORM to interact with the database. 
It allows me to work with Python objects instead of writing raw SQL queries, making database operations safer and easier to read.
I use it to store and retrieve users, posts, comments, and likes efficiently.

