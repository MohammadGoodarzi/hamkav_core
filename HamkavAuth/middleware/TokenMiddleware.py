# custom_middleware.py

from django.http import JsonResponse
from jwt.exceptions import ExpiredSignatureError

class JWTExceptionHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
            # response = self.get_response(request)
            # if response.status_code == 500:
            #     response = JsonResponse({"error": "Token expired"}, 
            #                  status=401)
            # return response;
        
        try:
            response = self.get_response(request)
            
            if response.status_code == 500:
                response = JsonResponse({"error": "Token expired"}, 
                             status=401)
            
            print(" =========>>>>")
            print(response)
            return response
        except ExpiredSignatureError:
            return JsonResponse(
                {"error": "Token expired"}, status=401
            )  


