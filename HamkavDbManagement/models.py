from django.db import models
from HamkavAuth.models import User
import jdatetime


import uuid

class Task(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class DataBaseType(models.Model):
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null= False, blank=False)
    name = models.CharField(max_length=300, null= False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
	    return f'{self.id} - {self.title} - {self.name}'
    

class DataBaseConnectionModel(models.Model):
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    database_type =  models.ForeignKey(DataBaseType, on_delete=models.CASCADE)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000, null=True, blank=True)
    title = models.CharField(max_length=300, null= False, blank=False)
    name = models.CharField(max_length=300, null= False, blank=False)
    port =models.PositiveIntegerField(null=False, blank=False)
    username = models.CharField(max_length=300, null= False, blank=False)
    password = models.CharField(max_length=300, null= False, blank=False)
    connection_string = models.CharField(max_length=1000, null= False, blank=False)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_shamsi = models.CharField(max_length=50, null=True, editable=False)
    updated_shamsi = models.CharField(max_length=50, null=True, editable=False)
    is_active = models.BooleanField(default=True)
    
    def save(self,  *args, **kwargs):
        self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
		# self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        super(DataBaseConnectionModel, self).save( *args, **kwargs)
    
    def __str__(self):
	    return f'{self.id} - {self.title} - {self.name}'
	    # return f'{self.database_type}-{self.id} - {self.title} - {self.name}'
    

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

class DataSourceModel(models.Model):
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    database_connection =  models.ForeignKey(DataBaseConnectionModel, on_delete=models.CASCADE)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null= False, blank=False)
    name = models.CharField(max_length=300, null= False, blank=False)
    query_string = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_shamsi = models.CharField(max_length=50, null=True, editable=False)
    updated_shamsi = models.CharField(max_length=50, null=True, editable=False)
    is_active = models.BooleanField(default=True)
    
    def save(self,  *args, **kwargs):
        self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
		# self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        super(DataSourceModel, self).save( *args, **kwargs)
    
    def __str__(self):
	    return f'{self.uuid} - {self.title} - {self.created}'
	    # return f'{self.database_type}-{self.id} - {self.title} - {self.name}'
    
