# #  this file must be imported in project settings file

# REST_FRAMEWORK = {
#         'DEFAULT_AUTHENTICATION_CLASSES': (
#                          'rest_framework_simplejwt.authentication.JWTAuthentication',
#                              )
#         }

from datetime import timedelta


INSTALLED_APPS = [

    'rest_framework_simplejwt',  
    'django-ninja',
    'ninja_jwt',
    'ninja_extra',
    
]

# jwt
from datetime import timedelta
# REST_FRAMEWORK = {
#     'DEFAULT_FILTER_BACKENDS': [
#         'django_filters.rest_framework.DjangoFilterBackend'
#     ],
# 'DEFAULT_AUTHENTICATION_CLASSES': (
    
#     'rest_framework.authentication.SessionAuthentication',
#     'rest_framework.authentication.BasicAuthentication',
#     'rest_framework_simplejwt.authentication.JWTAuthentication', 
# ),
# }


# CSRF_COOKIE_SECURE = False

# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
#     "ROTATE_REFRESH_TOKENS": False,
#     "BLACKLIST_AFTER_ROTATION": False,
#     "UPDATE_LAST_LOGIN": False,

#     "ALGORITHM": "HS256",
#     # "SIGNING_KEY": settings.SECRET_KEY,
#     "VERIFYING_KEY": "",
#     "AUDIENCE": None,
#     "ISSUER": None,
#     "JSON_ENCODER": None,
#     "JWK_URL": None,
#     "LEEWAY": 0,

#     "AUTH_HEADER_TYPES": ("Bearer",),
#     "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
#     "USER_ID_FIELD": "id",
#     # "USER_ID_CLAIM": "user_id",
#     "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

#     "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
#     "TOKEN_TYPE_CLAIM": "token_type",
#     "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

#     "JTI_CLAIM": "jti",

#     "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
#     "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
#     "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

#     "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
#     "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
#     "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
#     "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
#     "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
#     "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
    
#       # It will work instead of the default serializer(TokenObtainPairSerializer).
#      "TOKEN_OBTAIN_SERIALIZER": "HamkavAuth.serializers.MyTokenObtainPairSerializer",
# }