from django.db import models
# Create your models here.
from django.db import models
from HamkavAuth.models import User
import jdatetime
from treebeard.mp_tree import MP_Node


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