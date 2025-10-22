from fastapi import Body, FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models
from .database import engine, get_db
from .routers import post, user, auth, vote


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
# origins = [
#     "https://www.google.com",
#     "https://www.youtube.com",
#     "http://localhost",
#     "http://localhost:8000",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts
