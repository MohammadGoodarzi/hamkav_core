from ninja import Router
from ninja_jwt.authentication import JWTAuth  # jwt
from ninja import NinjaAPI,Form,Schema
from typing import List
from pydantic import UUID4



from .models import DataBaseConnectionModel, DataBaseType, Task
from . api_views import DB


router = Router()

class category_out(Schema):
    id: int
    name: str

class dbCconnectionItems(Schema):
    database_type_uuid: str
    url: str 
    title: str 
    name: str
    port: int 
    username: str 
    password: str 
    connection_string: str  = None
    description: str  = None
    
class DataBaseType_out(Schema):
    uuid: UUID4
    title: str
    name: str
    
class dbCconnectionItems_out(Schema):
    database_type: DataBaseType_out = None
    uuid: UUID4
    url: str 
    title: str 
    name: str
    port: int 
    username: str 
    password: str 
    connection_string: str  = None
    description: str  = None
class dbCconnectionItems_out_2(Schema):
    database_type: DataBaseType_out = None
    uuid: UUID4
    # url: str 
    title: str 
    # name: str
    # port: int 
    # username: str 
    # password: str 
    # connection_string: str  = None
    # description: str  = None

class datasourceItems(Schema):
    uuid: UUID4 = None # using for update method
    database_connection_uuid: UUID4
    title: str 
    name: str = None
    query_string: str 
    description: str  = None
    category: int 
    
class datasourceItems_out(Schema):
    # database_connection_uuid: dbCconnectionItems_out = None
    uuid: UUID4
    title: str 
    name: str = None
    query_string: str  = None
    description: str  = None
    category: category_out = None
    database_connection : dbCconnectionItems_out_2 = None
    

class sqlQueryText(Schema):
     query_string : str   
     database_connection_uuid : UUID4
     
     
    
@router.post("/AddNewConnection", auth=JWTAuth())
def create(request,dbCconnectionItems: dbCconnectionItems = Form(...)):

    a = DB(request)
    b = a.addNewConnection(dbCconnectionItems)
    return {"res":dbCconnectionItems,"ddd":"eeeeee"}

@router.post("/newdatasource", auth=JWTAuth())
def create(request,datasourceItems: datasourceItems = Form(...)):

    a = DB(request)
    b = a.addNewDatasource(datasourceItems)
    return {"res":datasourceItems,"ddd":"eeeeee"}

@router.get("/connections_list" , auth=JWTAuth(), response=List[dbCconnectionItems_out])
def list(request):
    a = DB(request)
    res = a.ConnectionList()
    return  res
    
@router.get("/datasource_detail", auth=JWTAuth(), response=datasourceItems_out)
def getDetail(request,uuid : UUID4):
    # print(uuid)
    a = DB(request)
    return a.GetDataSourceDetails(datasource_uuid = uuid)
    
@router.get("/datasources_list" , auth=JWTAuth(), response=List[datasourceItems_out])
def list(request):
    a = DB(request)
    res = a.DatasourceList()
    return  res

@router.get("/categorised_datasource_list")
def GetCategorisedDataSourceList(request):
    a = DB(request)
    res = a.GetCategorisedDataSourceList()
    # print(res)
    return  res

    
@router.post("/runquery", auth=JWTAuth())
def list(request, sqlQueryText:sqlQueryText = Form(...)):
    a = DB(request)
    res = a.RunQuery(sqlQueryText)
    return  {"res":res}

@router.get("/datasourceresult")
def list(request, datasource_uuid : UUID4):
    a = DB(request)
    res = a.GetDataSourceResult(datasource_uuid)
    return  {"res":res}
    
    # res = DataBaseConnectionModel.objects.select_related("database_type")
    # res = DataBaseConnectionModel.objects.filter(is_active = True)
    # for i in res:
    #     print(i)
    # print(res)
    # return  list(res)
    # dbconn = DbConnection(request)
    # result = dbconn.ConnectionList()
    # return result




# class UserSchema(Schema):
#     id: int
#     first_name: str
#     last_name: str

# class TaskSchema(Schema):
#     id: int
#     title: str
#     is_completed: bool
#     owner: UserSchema = None  # ! None - to mark it as optional


# @router.get("/tasks", response=List[TaskSchema])
# def tasks(request):
#     # return {"dd":"eee"}
#     # res = DataBaseConnectionModel.objects.filter(is_active = True)
#     # for i in res:
#     #     print(i)
        
#     queryset = Task.objects.select_related("owner")
#     for i in queryset:
#         print(i)
#     return list(queryset)






