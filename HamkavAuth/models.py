from typing import Optional
from django.db import models
# from users.models import MembershipStatus
from django.contrib.auth.models import  AbstractUser,AbstractBaseUser, PermissionsMixin
from .managers import UserManager
import uuid
# class User(AbstractUser):
# class User(AbstractBaseUser):
class User(AbstractBaseUser, PermissionsMixin):
    user_uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    country = models.CharField(verbose_name='country', max_length=255)
    full_name = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # status = models.ForeignKey(MembershipStatus, on_delete=models.SET_NULL, null=True, default=1)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'phone_number' # must be uniq
    REQUIRED_FIELDS = ['email','full_name'] # in createsuper command
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
    

class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'

    
# class HamkavAuthConfig(models.Model):
#     page_after_succesfull_login


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	age = models.PositiveSmallIntegerField(default=0)
	bio = models.TextField(null=True, blank=True)
 
 
 
class Relation(models.Model):
	from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
	to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.from_user} following {self.to_user}'