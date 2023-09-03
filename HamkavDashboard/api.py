from ninja import Router
from ninja_jwt.authentication import JWTAuth  # jwt
from ninja import NinjaAPI,Form,Schema
from typing import List
from pydantic import UUID4, Json


from .models import LayoutModel
from . api_views import Layout, Chart


router = Router()

class ChartModelItems(Schema):
    datasource_uuid : UUID4
    chart_type_uuid : UUID4
    title:str
    access: str
    description:str
    extra_config:str = None
    
class ChartModelItems_out(Schema):
    datasource_uuid : UUID4
    chart_type_uuid : UUID4
    uuid: UUID4
    access: str
    title: str 

class ChartTypeModelItems_out(Schema):
    uuid: UUID4
    title: str 
    name: str 
    thumbnail: str = None
    # base_config: str 
    # access: str 
    
@router.post("/add_chart", auth=JWTAuth())
def create(request,ChartModelItems: ChartModelItems = Form(...)):

    a = Chart(request)
    b = a.addNewChart(ChartModelItems)
    return {"res":ChartModelItems}


@router.get("/charts_list" , auth=JWTAuth(), response=List[ChartModelItems_out])
def list(request):
    a = Chart(request)
    res = a.GetChartsList()
    return  res

@router.get("/charts_type_list" , auth=JWTAuth(), response=List[ChartTypeModelItems_out])
def list(request):
    a = Chart(request)
    res = a.GetChartTypeList()
    host = request.META['HTTP_HOST']
    # return  res
    return  res