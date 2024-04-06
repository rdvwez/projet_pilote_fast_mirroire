from pydantic import BeseModel


class UserPostIn(BeseModel):
    body: str


class UserPost(UserPostIn):
    id: int
