from django.shortcuts import get_object_or_404
from .models import LayoutModel, ChartModel, ChartTypeModel, Category
from django.conf import settings
from HamkavDashboard.models import DataSourceModel
from HamkavAuth.models import User
import json

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

        # print(ChartModelItems.extra_config)
        chart_type = get_object_or_404(ChartTypeModel,uuid = ChartModelItems.chart_type_uuid )
        
        res = ChartModel.objects.create(
            user_creator = self.request.user,
            extra_config = ChartModelItems.extra_config[0], # for one more [] that recived!
            # datasource = datasource,
            chart_type = chart_type,
            title = ChartModelItems.title,
            description = ChartModelItems.description,
            access = ChartModelItems.access,
        )
        for i in ChartModelItems.datasource_uuid:
            dataset = get_object_or_404(DataSourceModel, uuid = i)
            res.datasource.add(dataset)

        return res
    
    def addNewLayout(self,LayoutModelItems):
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
            res = LayoutModel.objects.create(
                user_creator = self.request.user,
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
            # print(i.extra_config)
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
        # Convert root categories to the desired JSON format
        category_hierarchy_json = [get_category_hierarchy(category, 'pi pi-folder', 'pi pi-th-large') for category in root_categories]
        
        # category_hierarchy_in_model_json = [get_category_hierarchy_in_model(category,LayoutModel,"layout_category") for category in root_categories]
        # print(category_hierarchy_in_model_json)
        
        
        return  category_hierarchy_json
     
    def getLayoutDetail(self, layout_uuid):
        import json
        res = get_object_or_404(LayoutModel, is_active = True, uuid = layout_uuid)
        res.layout_config = json.dumps(res.layout_config)
        return res
        
#============================================================
#============================================================
def get_category_hierarchy(category, category_icon, item_icon):
   
    
    
    result = {
        "key": str(category.pk),
        "label": category.name,
        "icon": category_icon,
        "data": "category"
    }

    children = []
    for child in category.get_children():
 
        # print("////////// ",LayoutModel.objects.filter(category = child))
                                                 
        layout_children = [{"key": str(layout.uuid), "label": layout.title ,   "data": "item", "icon": item_icon} for layout in child.layout_category.all()]
        
        # print("child",child)
        # print("layout_children",layout_children)
        
        if layout_children:
            children.append({
                "key": str(child.id),
                "label": child.name,
                "icon": category_icon,
                "data": "category",
                "children": layout_children
            })
        else:
            children.append(get_category_hierarchy(child, category_icon, item_icon))

    if children:
        result["children"] = children

    return result

def get_category_hierarchy_in_model(category, model, model_related_string):

    fields = Category._meta.get_fields() # get all fields of Book model
    reverse_relations = [field for field in fields if field.is_relation and field.auto_created]

    # Extract the related model names
    reverse_relation_names = [field.related_model.__name__ for field in reverse_relations]
    reverse_relation_names = [field.related_name for field in reverse_relations]

    print(reverse_relation_names) 

    # for field in book_fields: # loop through all fields
    #     print(field)
    #     print(isinstance(field, ForeignObjectRel))
    #     if isinstance(field, ForeignObjectRel): # check if field is a reverse relation
    #         book_reverse_relations.append(field) # add field to reverse relations list
    # print(book_reverse_relations)
    # # for i in book_reverse_relations:
    # #     print(i.layout_category)
        
               
    result = {
        "key": str(category.pk),
        "label": category.name,
    }

    children = []
    for child in category.get_children():
 
        print("////////// ",LayoutModel.objects.filter(category = child))
                                                 
        model_children = [{"key": str(m.uuid), "label": m.title} for m in child.reverse_relation_names[0].all()]
        

        
        if model_children:
            children.append({
                "key": str(child.id),
                "label": child.name,
                "children": model_children
            })
        # else:
        #     children.append(get_category_hierarchy_in_model(category, model, model_related))

    if children:
        result["children"] = children

    return result


