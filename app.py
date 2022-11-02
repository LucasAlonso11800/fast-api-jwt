from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from pydantic import BaseModel, EmailStr
from functions_jwt import write_token, validate_token
from routes.users import users

app = FastAPI()
app.include_router(users)

load_dotenv()

class User(BaseModel):
    username: str
    email: EmailStr

@app.post("/login")
def login(user: User):
    if user.username == "Correct user":
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)

@app.post("/verify")
def verify(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token)