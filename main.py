from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()  


class Post(BaseModel):    
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title":"title of post1", "content":"content of post1","id":1},
    {"title":"title of post2", "content":"content of post2","id":2}    
]


@app.get("/")  
def root():    
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/posts")
def create_posts(post:Post):   
    post_dict = post.dict()
    post_dict['id'] = randrange(0,10000000)
    my_posts.append(post_dict)  
    return {"data":post_dict}