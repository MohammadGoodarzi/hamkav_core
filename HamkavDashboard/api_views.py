from django.shortcuts import get_object_or_404
from .models import LayoutModel, ChartModel, ChartTypeModel
from django.conf import settings
from HamkavDashboard.models import DataSourceModel
from HamkavAuth.models import User
# from . execSqlQuery import execPgQuery
from django.shortcuts import get_object_or_404 


from ninja_jwt.authentication import JWTAuth # jwt

class Layout:
    def __init__(self) -> None:
        pass    
    
    def addNewLayout(self,config):
        pass
    
    def updateLayout(self,uuid,config):
        pass
    
    def deleteLayout(self,uuid):
        pass
    
    def getLayout(self,uuid):
        pass
    
    def getLayoutList(self):
        pass
    
class Chart:
    def __init__(self, request):
        self.request = request
        
    def addNewChart(self,ChartModelItems):
        datasource = get_object_or_404(DataSourceModel,uuid = ChartModelItems.datasource_uuid )
        chart_type = get_object_or_404(ChartTypeModel,uuid = ChartModelItems.chart_type_uuid )
        
        res = ChartModel.objects.create(
            user_creator = self.request.user,
            datasource = datasource,
            chart_type = chart_type,
            title = ChartModelItems.title,
            description = ChartModelItems.description,
            access = ChartModelItems.access,
        )
        # print(res)
        return res
    
    def GetChartList(self):
        # res = DataSourceModel.objects.select_related("database_connection")
        res = ChartModel.objects.filter(is_active = True)
        # print(res)
        return  list(res)
    
    def GetChartDetail(self, chart_uuid):
        # res = DataSourceModel.objects.select_related("database_connection")
        # res = ChartModel.objects.filter(is_active = True, uuid = chart_uuid)
        res = get_object_or_404(ChartModel, is_active = True, uuid = chart_uuid)
        # print(res)
        return  res
      
    def GetChartTypeList(self):
        res = ChartTypeModel.objects.filter(is_active = True)
        
        
        # host = self.request.META['HTTP_HOST']
        # for r in res:
        #     r.thumbnail = 'ddddddd'
        #     print(r.thumbnail.url)
        #     print( r.thumbnail.path )
        # #     if r.thumbnail.url:
        # #         r.thumbnail = self.request.build_absolute_uri(r.thumbnail.url)#'wwwww' + r.thumbnail.url
        # #     # print( r.thumbnail )
        # #     # print( r.thumbnail.url )
        # #     # print("*******************")
        # # #     # print( r.get_absolute_url() )
        
        
        #     if r.thumbnail:
        #         r.thumbnail = self.request.build_absolute_uri(r.thumbnail.url)#'wwwww' + r.thumbnail.url
        #         # print(r.thumbnail.url.r.thumbnail.replace(settings.MEDIA_URL, '', 1))
        #         # print(r.thumbnail)
            
        #     # Remove the '/media/' prefix from the URL
        #         print(r.thumbnail.url.replace(settings.MEDIA_URL, '', 1))
        #         r.thumbnail =  r.thumbnail.url.replace(settings.MEDIA_URL, '', 1)
            
        
        return  list(res)



