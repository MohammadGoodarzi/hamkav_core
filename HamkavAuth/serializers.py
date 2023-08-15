# users/serializers.py 
from rest_framework import serializers
from.models import User

# class UserSerializer(serializers.ModelSerializer):
#     date_joined = serializers.ReadOnlyField()
#     class Meta(object):
#         model = User
#         fields = ('id', 'email', 'first_name', 'last_name',
#                   'date_joined', 'password')
#         extra_kwargs = {'password': {'write_only': True}}
        
        
     
     
#==================== jwt token ======================    

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['full_name'] = user.full_name
        token['user_uuid'] = str(user.user_uuid)
        # ...

        return token
    
   