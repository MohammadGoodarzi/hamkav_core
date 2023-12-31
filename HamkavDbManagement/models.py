from django.db import models
from HamkavAuth.models import User
import jdatetime
from HamkavConfigurator.models import Category_type2 as Category
from HamkavMedia.models import MediaModel



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
    created_shamsi = models.CharField(max_length=50, null=True, editable=False)
    updated_shamsi = models.CharField(max_length=50, null=True, editable=False)
    is_active = models.BooleanField(default=True)
    
    def save(self,  *args, **kwargs):
        self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
		# self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        super(DataBaseType, self).save( *args, **kwargs)
        
    
    def __str__(self):
	    return f'{self.id} - {self.title} - {self.name}'
    

class DataBaseConnectionModel(models.Model):
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    database_type =  models.ForeignKey(DataBaseType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="database_category")
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

class DataSourceType(models.Model):
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null= False, blank=False)
    name = models.CharField(max_length=300, null= False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_shamsi = models.CharField(max_length=50, null=True, editable=False)
    updated_shamsi = models.CharField(max_length=50, null=True, editable=False)
    is_active = models.BooleanField(default=True)
    
    def save(self,  *args, **kwargs):
        self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
		# self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        super(DataSourceType, self).save( *args, **kwargs)
        
    
    def __str__(self):
	    return f'{self.id} - {self.title} - {self.name}'

class DataSourceModel(models.Model):
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    database_connection =  models.ForeignKey(DataBaseConnectionModel, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="datasource_category")
    datasource_type = models.ForeignKey(DataSourceType, on_delete=models.CASCADE, null=True, blank=True)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    media_source = models.ForeignKey(MediaModel, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300, null= False, blank=False)
    name = models.CharField(max_length=300, null= True, blank=True)
    query_string = models.TextField(null=True, blank=True)
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
	    return f'{self.uuid} - {self.title} - {self.created} - {self.media_source}'
	    # return f'{self.database_type}-{self.id} - {self.title} - {self.name}'
    
class APIManageModel(models.Model):
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True,unique=False)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null= False, blank=False)
    url = models.CharField(max_length=300, null= False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    created_shamsi = models.CharField(max_length=50, null=True, editable=False)
    updated_shamsi = models.CharField(max_length=50, null=True, editable=False)
    
    def save(self,  *args, **kwargs):
        self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
		# self.created_shamsi = jdatetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        super(APIManageModel, self).save( *args, **kwargs)
    def __str__(self):
	    return f'{self.id} - {self.title} - {self.url}'