from django.db import models
from HamkavAuth.models import User

import uuid


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
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
	    return f'{self.id} - {self.title} - {self.name}'
    

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
