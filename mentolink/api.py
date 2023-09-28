
from ninja import NinjaAPI
from ninja.security import HttpBasicAuth
from HamkavAuth.api import router as HamkavAuth_router
from HamkavDbManagement.api import router as HamkavDbManagement_router
from HamkavDashboard.api import router as HamkavDashboard_router
from HamkavConfigurator.api import router as HamkavConfigurator_router

from ninja_jwt.controller import NinjaJWTDefaultController    # jwt
from ninja_extra import NinjaExtraAPI  # jwt
from ninja_jwt.authentication import JWTAuth # jwt


class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, phone_number, password):
        if phone_number == "09158110553" and password == "1234":
            return phone_number
        
        

# api = NinjaAPI()
api = NinjaExtraAPI() # jwt
api.register_controllers(NinjaJWTDefaultController) # jwt

# from ninja_jwt.exceptions import TokenError
# from rest_framework.exceptions import AuthenticationFailed
# @api.exception_handler(TokenError)
# def handle_token_error(request, exc):
# return api.create_response(request, {"detail": "Token has expired"}, status=401)


api.add_router("/auth",HamkavAuth_router, tags=["auth"])
# api.add_router("/db_management",HamkavDbManagement_router, auth=JWTAuth() ,tags=["db_management"])
api.add_router("/db_management",HamkavDbManagement_router,tags=["db_management"])
api.add_router("/dashboard",HamkavDashboard_router,tags=["dashboard"])
api.add_router("/configurator",HamkavConfigurator_router,tags=["configurator"])

# @api.get("/add")
# def add(request, a: int, b: int):
#     return {"result": a + b}



