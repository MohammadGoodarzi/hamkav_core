from collections.abc import Iterable
from django.db import models
# Create your models here.
from django.db import models
from HamkavAuth.models import User
import jdatetime
from treebeard.mp_tree import MP_Node
from django.utils.text import slugify


import uuid

        

class Category(MP_Node):
    name = models.CharField(max_length=200)
    node_order_by = ['name']
    
    class Meta:
        verbose_name = 'دسته بندی داشبورد و چارت ها'
        verbose_name_plural = 'دسته بندی داشبورد و چارت ها'

    def __str__(self):
        return self.name
    
    
class Category_type2(MP_Node):
    name = models.CharField(max_length=200)
    node_order_by = ['name']

    class Meta:
        verbose_name = 'دسته بندی منبع داده'
        verbose_name_plural = 'دسته بندی منبع داده'
        
    def __str__(self):
        return self.name
    
    
class Category_type3(MP_Node):
    name = models.CharField(max_length=200)

    node_order_by = ['name']

    def __str__(self):
        return self.name
    
 
class BaseModel(models.Model):
    # Common fields that you want in every model
    # id = models.AutoField(primary_key=True)
    uuid =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False,unique=True)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE, null =True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_shamsi = models.CharField(max_length=50, null=True, editable=False)
    updated_shamsi = models.CharField(max_length=50, null=True, editable=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
               
        
class Attribute(BaseModel):
    name = models.CharField(max_length=500, null= False, blank=True,unique=True)
    title = models.CharField(max_length=500, null= False, blank=True)
    type = models.CharField(max_length=500, null= True, blank=True)
    description = models.CharField(max_length=500, null= True, blank=True)
    
    class meta:
        db_table = 'attribute'
        # verbose_name = " تعاریف سیستم "
        # verbose_name_plural = " تعاریف سیستم "
        
    def save(self) -> None:
        self.name = slugify(self.name,allow_unicode=True)
        return super().save()

    def __str__(self) :
        return self.name
        
class AttributeItems(BaseModel):
    attribute = models.ForeignKey(Attribute, on_delete = models.CASCADE, null = False)
    item_name = models.CharField(max_length=500, null= False, blank=True, unique=True)
    item_title = models.CharField(max_length=500, null= False, blank=True)
    item_code = models.CharField(max_length=500, null= False, blank=True)
    description = models.CharField(max_length=500, null= True, blank=True)
    
    class meta:
        db_table = 'attribute_items'
        # verbose_name = "  آیتم های تعاریف سیستم" 
        # verbose_name_plural ="  آیتم های تعاریف سیستم" 
    def save(self) -> None:
        self.name = slugify(self.item_name,allow_unicode=True)
        return super().save()
        
    def __str__(self) :
        return self.item_title
        
        
        
        
        
        