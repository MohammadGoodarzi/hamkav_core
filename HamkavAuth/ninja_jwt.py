# from typing import Any, Optional
# from django.http import HttpRequest
# from ninja.security import HttpBearer
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from ninja import Schema

# class JWTAuthRequired(HttpBearer):
#     def authenticate(self, request: HttpRequest, token: str) -> Optional[Any]:
#         jwt_authenticator = JWTAuthentication()
#         try:
#             response = jwt_authenticator.authenticate(request)
#             if response is not None:
#                 return True # 200 OK
#             return False # 401
#         except Exception:
#             # Any exception we want it to return False i.e 401
#             return False
  
  
# #   As for the creation of tokens, its a fairly simple approach also. I have 2 schemas one for 
# # the auth and one for the repsonse:             
# class AuthSchema(Schema):
#     username: str
#     password: str


# class JWTPairSchema(Schema):
#     refresh: str
#     access: str
    
