from fastapi import Request
from functions_jwt import validate_token
from fastapi.routing import APIRoute

class VerifyTokenRoute(APIRoute):
    def get_route_handler(self):
        original_route = super().get_route_handler()
        
        async def verify_token_middleware(request:Request):
            token = request.headers["Authorization"].split(" ")[1]
            
            validation_response = validate_token(token)

            if validation_response["error"] == True:
                return validation_response
            else:
                return await original_route(request)

        return verify_token_middleware