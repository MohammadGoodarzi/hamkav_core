
from ninja import NinjaAPI
from HamkavAuth.api import router as HamkavAuth_router
from HamkavDbManagement.api import router as HamkavDbManagement_router
from HamkavDashboard.api import router as HamkavDashboard_router
from HamkavConfigurator.api import router as HamkavConfigurator_router
from HamkavMedia.api import router as HamkavMedia_router

from ninja_jwt.controller import NinjaJWTDefaultController    # jwt
from ninja_extra import NinjaExtraAPI  # jwt
from ninja_jwt.authentication import JWTAuth # jwt

from HamkavAuth.utils.custom_ninja_auth import NinjaJwtCustomAuth, ApiKey
from ninja_extra import exceptions


# api = NinjaAPI()
api = NinjaExtraAPI() # jwt
api.register_controllers(NinjaJWTDefaultController) # jwt

# from ninja_jwt.exceptions import TokenError
# from rest_framework.exceptions import AuthenticationFailed
# @api.exception_handler(TokenError)
# def handle_token_error(request, exc):
# return api.create_response(request, {"detail": "Token has expired"}, status=401)

# header_key = NinjaJwtCustomAuth()

# def api_exception_handler(request, exc):
#     headers = {}

#     if isinstance(exc.detail, (list, dict)):
#         data = exc.detail
#     else:
#         data = {"detail": exc.detail}

#     response = api.create_response(request, data, status=exc.status_code)
#     for k, v in headers.items():
#         response.setdefault(k, v)

#     return response

# api.exception_handler(exceptions.APIException)(api_exception_handler)

api.add_router("/auth",HamkavAuth_router, tags=["auth"])
api.add_router("/db_management",HamkavDbManagement_router, auth=JWTAuth(), tags=["db_management"])
api.add_router("/dashboard",HamkavDashboard_router , auth=JWTAuth(), tags=["dashboard"])
api.add_router("/configurator",HamkavConfigurator_router, auth=JWTAuth(), tags=["configurator"])
api.add_router("/media",HamkavMedia_router, auth=JWTAuth(), tags=["media"])
# api.add_router("/configurator",HamkavConfigurator_router,auth=NinjaJwtCustomAuth(), tags=["configurator"])
 