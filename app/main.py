from fastapi import FastAPI

from app.models.post import UserPost, UserPostIn

app = FastAPI()


post_table = {}


@app.post("/", response_model=UserPost)
async def create_post(post: UserPostIn):
    data = post.dict()
    last_record_id = len(data)

    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post


@app.post("/post", response_model=list[UserPost])
async def get_all_posts():
    return list(post_table.values())
    return list(post_table.values())
