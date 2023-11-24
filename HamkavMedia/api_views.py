from HamkavAuth.models import User
from django.shortcuts import get_object_or_404
from .models import MediaModel,MediaTypeModel


from HamkavConfigurator.models import Category_type2
from HamkavConfigurator.api_views import get_category_hierarchy_in_model_relation



class Media:
    def __init__(self, request):
        self.request = request
        
    def GetMediaList(self):
        res = MediaModel.objects.filter(is_active = True)
        return  list(res)
    
    def GetMediaDetail(self, uuid):
        res = get_object_or_404(MediaModel, uuid = uuid)
        
        return res
  