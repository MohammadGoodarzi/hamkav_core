from django.db import models
from HamkavAuth.models import User
from django.contrib.auth.models import Group
from HamkavDbManagement.models import DataSourceModel
import jdatetime


import uuid



class LayoutModel(models.Model):
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null= False, blank=False)
    description = models.CharField(max_length=1000, null= True, blank=True)
    
    name = models.CharField(max_length=300, null= True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    layout_config = models.JSONField(null=True, blank=True, max_length=2000)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_shamsi = models.CharField(max_length=50, null=True, editable=False)
    updated_shamsi = models.CharField(max_length=50, null=True, editable=False)
    is_active = models.BooleanField(default=True)
    
    def save(self,  *args, **kwargs):
        self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
		# self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        super(LayoutModel, self).save( *args, **kwargs)
    
    def __str__(self):
	    return f'{self.id} - {self.title} - {self.name}'
 
 
class ChartTypeModel(models.Model):
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=300, null= True, blank=True)
    name = models.CharField(max_length=300, null= True, blank=True)
    access = models.CharField(max_length=300, null= True, blank=True)
    base_config = models.JSONField(null=True, blank=True, max_length=2000)
    thumbnail = models.ImageField(upload_to='attach/%Y/%m/%d' ,null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_shamsi = models.CharField(max_length=50, null=True, editable=False)
    updated_shamsi = models.CharField(max_length=50, null=True, editable=False)
    is_active = models.BooleanField(default=True)
    
    def save(self,  *args, **kwargs):
        self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
		# self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        super(ChartTypeModel, self).save( *args, **kwargs)
        
    def __str__(self):
	    return f'{self.id} - {self.title} - {self.user_creator} - {self.created_shamsi}'
 
class ChartModel(models.Model):
    
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    chart_type = models.ForeignKey(ChartTypeModel, on_delete=models.CASCADE, null=True)
    datasource = models.ForeignKey(DataSourceModel, on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=300, null= False, blank=False)
    # chart_type_title = models.CharField(max_length=300, null= True, blank=True)
    description = models.CharField(max_length=1000, null= True, blank=True)
    extra_config = models.JSONField(null=True, blank=True, max_length=2000)
    access = models.CharField(max_length=300, null= True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_shamsi = models.CharField(max_length=50, null=True, editable=False)
    updated_shamsi = models.CharField(max_length=50, null=True, editable=False)
    is_active = models.BooleanField(default=True)
    
    def save(self,  *args, **kwargs):
        self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
		# self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        super(ChartModel, self).save( *args, **kwargs)
        
    def __str__(self):
	    return f'{self.id} - {self.title}  - {self.created_shamsi} - ||| {self.chart_type.title} '

    	# def get_absolute_url(self):
		# return reverse("HamkavBlog:category_detail", args=(self.id, self.slug))
	
