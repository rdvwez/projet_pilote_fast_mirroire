from pydantic import BeseModel


class UserPostIn(BeseModel):
    body: str


class UserPost(UserPostIn):
    id: int


class CommentIn(BeseModel):
    body: str
    post_id: int


class Comment(CommentIn):
    id: int


class UserPostWithComments(BeseModel):
    post: UserPost
    comments: list[Comment]
