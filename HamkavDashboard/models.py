from django.db import models
from HamkavAuth.models import User
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
 
 
class ChartModel(models.Model):
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    datasource = models.ForeignKey(DataSourceModel, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300, null= False, blank=False)
    description = models.CharField(max_length=1000, null= True, blank=True)
    
    name = models.CharField(max_length=300, null= True, blank=True)
    chart_type_id = models.PositiveSmallIntegerField(null=True)
    chart_type_title = models.CharField(max_length=300, null= True, blank=True)
    chart_base_config = models.JSONField(max_length=100, null=True, blank=True)
    chart_access = models.CharField(max_length=20, null=True, blank=True)
    chart_additional_config = models.JSONField(null=True, blank=True, max_length=2000)

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
	    return f'{self.id} - {self.title} - {self.chart_type_title} - - {self.created_shamsi}'