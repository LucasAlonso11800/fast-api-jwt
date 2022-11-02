from fastapi import APIRouter
from pydantic import BaseModel
from requests import get
from middleware import VerifyTokenRoute

users= APIRouter(route_class=VerifyTokenRoute)

class UserGithub(BaseModel):
    country: str
    page: str

@users.post("/users/github")
def github_users(github: UserGithub):
    return get(f'https://api.github.com/search/users?q=location:"{github.country}"&page={github.page}').json()