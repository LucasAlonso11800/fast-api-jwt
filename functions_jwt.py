from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from os import getenv
from fastapi.responses import JSONResponse

def write_token(data: dict):
    payload = {
        **data, 
        "exp": datetime.now() + timedelta(hours=4)
    }
    token = encode(payload=payload, key=getenv("SECRET"), algorithm="HS256")
    return token

def validate_token(token: str):
    try:
        data = decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        return {"error": False, **data }
    except exceptions.DecodeError:
        return JSONResponse(content={"error": True, "message": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"error": True, "message": "Token Expired"}, status_code=401)