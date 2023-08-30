from django.shortcuts import get_object_or_404
from .models import LayoutModel, ChartModel
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
        
        res = ChartModel.objects.create(
            user_creator = self.request.user,
            datasource = datasource,
            title = ChartModelItems.title,
            description = ChartModelItems.description,
            chart_type_id= ChartModelItems.chart_type_id,
            chart_type_title= ChartModelItems.chart_type_title,
            chart_access = ChartModelItems.chart_access,
        )
        print(res)
        return res
    
    def getChartList(self, ChartModelItems):
        pass    
