from django.db import models
from HamkavConfigurator.models import Category_type3
from HamkavAuth.models import User
import jdatetime
import uuid

class MediaTypeModel(models.Model):
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    title = models.CharField(max_length=300, null= False, blank=False)
    extension = models.CharField(max_length=10, null= False, blank=False)
    description = models.CharField(max_length=1000, null= True, blank=True)
    access = models.CharField(max_length=300, null= True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_shamsi = models.CharField(max_length=50, null=True, editable=False)
    updated_shamsi = models.CharField(max_length=50, null=True, editable=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
	    return f'{self.title}'

class MediaModel(models.Model):
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    category = models.ForeignKey(Category_type3, on_delete=models.CASCADE, null=True, related_name="images_category")
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    media_url = models.ImageField(upload_to='attach/%Y/%m/%d' ,null=False, blank=False)
    type = models.ForeignKey(MediaTypeModel, on_delete=models.CASCADE, related_name="Media_MediaType")
    title = models.CharField(max_length=300, null= False, blank=False)
    description = models.CharField(max_length=1000, null= True, blank=True)
    access = models.CharField(max_length=300, null= True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_shamsi = models.CharField(max_length=50, null=True, editable=False)
    updated_shamsi = models.CharField(max_length=50, null=True, editable=False)
    is_active = models.BooleanField(default=True)
    
    def save(self,  *args, **kwargs):
        self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
		# self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        super(MediaModel, self).save( *args, **kwargs)
    
    def __str__(self):
	    return f'{self.title}'
    