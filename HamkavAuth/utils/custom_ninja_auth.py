from ninja.security import APIKeyHeader
from ninja_jwt.authentication import JWTBaseAuthentication
from ninja.security import HttpBasicAuth
from rest_framework_simplejwt.authentication import JWTAuthentication



class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, phone_number, password):
        if phone_number == "09158110553" and password == "1234":
            return phone_number
        
class NinjaJwtCustomAuth(APIKeyHeader, JWTBaseAuthentication):
    print('*'*100)
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        print(self.jwt_authenticate(request, token=key))
        return self.jwt_authenticate(request, token=key)
    
    
    
class ApiKey(APIKeyHeader, JWTBaseAuthentication):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        return self.jwt_authenticate(request, token=key)
    
    

# class CustomJWTAuthentication(JWTAuthentication):
#     def verify_token(self, token):
#         # Add your custom token validation logic here
#         # Return True if the token is valid; otherwise, return False
#         if custom_validation_check(token):
#             return True
#         return False
