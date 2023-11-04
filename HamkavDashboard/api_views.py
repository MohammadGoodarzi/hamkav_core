from django.shortcuts import get_object_or_404
from .models import LayoutModel, ChartModel, ChartTypeModel

from HamkavConfigurator.models import Category

from django.conf import settings
from HamkavDashboard.models import DataSourceModel
from HamkavAuth.models import User
from HamkavConfigurator.api_views import get_category_hierarchy_in_model_relation
# from HamkavConfigurator.utils import get_category_one_hierarchy 
import json

# from . execSqlQuery import execPgQuery
from django.shortcuts import get_object_or_404 


from ninja_jwt.authentication import JWTAuth # jwt

# class Layout:
#     def __init__(self) -> None:
#         pass    
    
#     def addNewLayout(self,config):
#         pass
    
#     def updateLayout(self,uuid,config):
#         pass
    
#     def deleteLayout(self,uuid):
#         pass
    
#     def getLayout(self,uuid):
#         pass
    
#     def getLayoutList(self):
#         pass
    
class Chart:
    def __init__(self, request):
        self.request = request
        
    # def addNewChart(self,ChartModelItems):

    #     # print(ChartModelItems.extra_config)
    #     chart_type = get_object_or_404(ChartTypeModel,uuid = ChartModelItems.chart_type_uuid )
    #     cat = get_object_or_404(Category,id =ChartModelItems.category) 
        
        
    #     res = ChartModel.objects.create(
    #         user_creator = self.request.user,
    #         extra_config = ChartModelItems.extra_config[0], # for one more [] that recived!
    #         # datasource = datasource,
    #         chart_type = chart_type,
    #         title = ChartModelItems.title,
    #         description = ChartModelItems.description,
    #         access = ChartModelItems.access,
    #         category = cat,
            
    #     )
    #     for i in ChartModelItems.datasource_uuid:
    #         dataset = get_object_or_404(DataSourceModel, uuid = i)
    #         res.datasource.add(dataset)

    #     return res
    
    
    def AddUpdateChart(self,ChartModelItems):

        # print(ChartModelItems.extra_config)
        chart_type = get_object_or_404(ChartTypeModel,uuid = ChartModelItems.chart_type_uuid )
        cat = get_object_or_404(Category,id =ChartModelItems.category) 
        
        
        # res = ChartModel.objects.create(
        #         user_creator = self.request.user,
        #         extra_config = ChartModelItems.extra_config[0], # for one more [] that recived!
        #         chart_type = chart_type,
        #         title = ChartModelItems.title,
        #         description = ChartModelItems.description,
        #         access = ChartModelItems.access,
        #         category = cat,
        #     )
                    
        # print(ChartModelItems.uuid)
        if not ChartModelItems.uuid :
            res = ChartModel.objects.create(
                user_creator = self.request.user,
                extra_config = ChartModelItems.extra_config[0], # for one more [] that recived!
                chart_type = chart_type,
                title = ChartModelItems.title,
                description = ChartModelItems.description,
                access = ChartModelItems.access,
                category = cat,
            )
        else:
            res = ChartModel.objects.filter(uuid = ChartModelItems.uuid).update(
                user_creator = self.request.user,
                extra_config = ChartModelItems.extra_config[0], # for one more [] that recived!
                chart_type = chart_type,
                title = ChartModelItems.title,
                description = ChartModelItems.description,
                access = ChartModelItems.access,
                category = cat,
            )
            res = ChartModel.objects.filter(uuid = ChartModelItems.uuid)[0]
            res.datasource.clear()
   
        for i in ChartModelItems.datasource_uuid:
            dataset = get_object_or_404(DataSourceModel, uuid = i)
            res.datasource.add(dataset)

        return res
    
    
    def addNewLayout(self,LayoutModelItems):
        # print(LayoutModelItems.category)
        if LayoutModelItems.uuid :
           res = LayoutModel.objects.filter(uuid = LayoutModelItems.uuid ).update(
                # user_creator = self.request.user,
                title = LayoutModelItems.title,
                description = LayoutModelItems.description,
                type = LayoutModelItems.type,
                layout_config = LayoutModelItems.layout_config,
                access = LayoutModelItems.access,
           )
           return res
        else:


            # print("LayoutModelItems.category",LayoutModelItems.category)
            cat = get_object_or_404(Category,id =LayoutModelItems.category) 
            print(cat, cat.name)
            res = LayoutModel.objects.create(
                user_creator = self.request.user,
                category = cat,
                title = LayoutModelItems.title,
                description = LayoutModelItems.description,
                type = LayoutModelItems.type,
                layout_config = LayoutModelItems.layout_config,
                access = LayoutModelItems.access,
            )
        # print(res)
        return res
    
    def GetChartList(self):
        # res = DataSourceModel.objects.select_related("database_connection")
        res = ChartModel.objects.filter(is_active = True)
        
        for i in res:
            i.extra_config = json.dumps(i.extra_config)
            
            # if i.category:
            #     i.category = i.category.__str__()
            # else:
            #     i.category = None
                
            # print(type(i.extra_config))
        # print(res)
        return  list(res)
    
    def GetChartDetail(self, chart_uuid):
        # res = DataSourceModel.objects.select_related("database_connection")
        # res = ChartModel.objects.filter(is_active = True, uuid = chart_uuid)
        res = get_object_or_404(ChartModel, is_active = True, uuid = chart_uuid)
        res.extra_config = json.dumps(res.extra_config)
        # print(res)
        return  res
      
    def GetChartTypeList(self):
        res = ChartTypeModel.objects.filter(is_active = True)

        return  list(res)

    def GetLayoutsList(self):
        # res = DataSourceModel.objects.select_related("database_connection")
        res = LayoutModel.objects.filter(is_active = True)
        return  list(res)
   
    def GetCategorisedLayoutsList(self):
   
        root_categories = Category.get_root_nodes()
        # print(root_categories)
        category_hierarchy_json = [get_category_hierarchy_in_model_relation(category, 'layout_category', 'pi pi-folder', 'pi pi-th-large') for category in root_categories]
        return  category_hierarchy_json
    
    def getLayoutDetail(self, layout_uuid):
        import json
        res = get_object_or_404(LayoutModel, is_active = True, uuid = layout_uuid)
        res.layout_config = json.dumps(res.layout_config)
        return res
        



