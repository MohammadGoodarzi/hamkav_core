from ninja import Router
from ninja_jwt.authentication import JWTAuth  # jwt
from ninja import NinjaAPI,Form,Schema
from typing import List
from pydantic import UUID4

from .models import MediaModel,MediaTypeModel
from . api_views import Media

router = Router()

class MediaType_out(Schema):
    uuid: UUID4
    title: str 
    extension: str 
    description: str  = None
   
    
class Media_out(Schema):
    uuid: UUID4
    title: str 
    description: str  = None
    media_url: str
    created_shamsi: str
    # user_creator: str
    type: MediaType_out = None
    
@router.get("/media_list" , auth=JWTAuth(), response=List[Media_out])
def list(request):
    a = Media(request)
    res = a.GetMediaList()
    return  res
    
@router.get("/media_detail", auth=JWTAuth(), response=Media_out)
def getDetail(request,uuid : UUID4):
    # print(uuid)
    a = Media(request)
    return a.GetMediaDetail(uuid = uuid)

#==========

    
# @router.post("/AddNewConnection", auth=JWTAuth())
# def create(request,dbCconnectionItems: dbCconnectionItems = Form(...)):

#     a = DB(request)
#     b = a.addNewConnection(dbCconnectionItems)
#     return {"res":dbCconnectionItems,"ddd":"eeeeee"}

# @router.post("/newdatasource", auth=JWTAuth())
# def create(request,datasourceItems: datasourceItems = Form(...)):

#     a = DB(request)
#     b = a.addNewDatasource(datasourceItems)
#     return {"res":datasourceItems,"ddd":"eeeeee"}


    
# @router.get("/datasources_list" , auth=JWTAuth(), response=List[datasourceItems_out])
# def list(request):
#     a = DB(request)
#     res = a.DatasourceList()
#     return  res

# @router.get("/categorised_datasource_list")
# def GetCategorisedDataSourceList(request):
#     a = DB(request)
#     res = a.GetCategorisedDataSourceList()
#     # print(res)
#     return  res

    
# @router.post("/runquery", auth=JWTAuth())
# def list(request, sqlQueryText:sqlQueryText = Form(...)):
#     a = DB(request)
#     res = a.RunQuery(sqlQueryText)
#     return  {"res":res}

# @router.get("/datasourceresult")
# def list(request, datasource_uuid : UUID4):
#     a = DB(request)
#     res = a.GetDataSourceResult(datasource_uuid)
#     return  {"res":res}
    
#     # res = DataBaseConnectionModel.objects.select_related("database_type")
#     # res = DataBaseConnectionModel.objects.filter(is_active = True)
#     # for i in res:
#     #     print(i)
#     # print(res)
#     # return  list(res)
#     # dbconn = DbConnection(request)
#     # result = dbconn.ConnectionList()
#     # return result




# # class UserSchema(Schema):
# #     id: int
# #     first_name: str
# #     last_name: str

# # class TaskSchema(Schema):
# #     id: int
# #     title: str
# #     is_completed: bool
# #     owner: UserSchema = None  # ! None - to mark it as optional


# # @router.get("/tasks", response=List[TaskSchema])
# # def tasks(request):
# #     # return {"dd":"eee"}
# #     # res = DataBaseConnectionModel.objects.filter(is_active = True)
# #     # for i in res:
# #     #     print(i)
        
# #     queryset = Task.objects.select_related("owner")
# #     for i in queryset:
# #         print(i)
# #     return list(queryset)






