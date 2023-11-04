# # your_app/utils/custom_exception_handler.py

# from rest_framework.views import exception_handler
# from rest_framework_simplejwt.exceptions import TokenError

# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)

#     if isinstance(exc, TokenError):
#         # Handle token expiration error here
#         response.data = {
#             'error': 'Token is expired',
#             'status_code': 401  # or any other status code you prefer
#         }
#         response.status_code = 401  # Set the desired status code

#     return response
