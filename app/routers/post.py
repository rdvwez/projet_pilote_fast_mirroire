from fastapi import APIRouter, HTTPException

from app.models.post import (
    Comment,
    CommentIn,
    UserPost,
    UserPostIn,
    UserPostWithComments,
)

router = APIRouter()
post_table = {}
comment_table = {}


def find_post(post_id: int):
    return post_table.get(post_id)


@router.post("/", response_model=UserPost)
async def create_post(post: UserPostIn):
    data = post.dict()
    last_record_id = len(data)

    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post


@router.post("/post", response_model=list[UserPost])
async def get_all_posts():
    return list(post_table.values())


@router.post("/comment", response_model=Comment, status_code=201)
async def create_comment(comment: CommentIn):
    post = find_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    data = comment.dict()
    last_record_id = len(comment_table)

    new_comment = {**data, "id": last_record_id}
    comment_table[last_record_id] = new_comment
    return new_comment


@router.post("/post/{post_id}/comment", response_model=list[Comment])
async def get_comment_on_post(post_id: int):
    return [
        Comment for comment in comment_table.values() if comment["post_id"] == post_id
    ]


@router.post("/post/{post_id}", response_model=UserPostWithComments)
async def get_post_with_comments(post_id: int):
    post = find_post(post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return {
        "post": post,
        "comment": await get_comment_on_post(post_id),
    }
