from ninja import Router
from ninja_jwt.authentication import JWTAuth  # jwt
from ninja import NinjaAPI,Form,Schema
from typing import List
from pydantic import UUID4, Json


from .models import LayoutModel
from . api_views import Layout, Chart
from HamkavDbManagement.api import datasourceItems_out


router = Router()
a = "testss"

class ChartModelItems(Schema):
    datasource_uuid : UUID4
    chart_type_uuid : UUID4
    title:str
    access: str
    description:str
    extra_config:str = None
    
class LayoutModelItems(Schema):
    title:str
    access: str = None
    description:str = None
    type:str = None
    layout_config: Json = None
    # Layout_config: Json = None
       
class ChartTypeModelItems_out(Schema):
    uuid: UUID4
    title: str 
    name: str 
    thumbnail: str = None
    meta_info: str = None
    # base_config: str 
    # access: str 
    
class ChartModelItems_out(Schema):
    uuid: UUID4
    # datasource_id: int
    datasource: datasourceItems_out
    chart_type: ChartTypeModelItems_out #if a=="test" else None
    # datasource: List [datasourceItems_out]
    # chart_type_uuid 
    access: str
    title: str 

# Chart    
@router.post("/add_chart", auth=JWTAuth())
def create(request,ChartModelItems: ChartModelItems = Form(...)):
    a = Chart(request)
    b = a.addNewChart(ChartModelItems)
    return {"res":ChartModelItems}


@router.get("/chart_list" , auth=JWTAuth(), response=List[ChartModelItems_out])
def list(request):
    # delattr(ChartModelItems_out, "title") 
    # ChartModelItems_out.ddd = ChartModelItems_out.create_field("ddd", str, None)
    a = Chart(request)
    res = a.GetChartList()
    return  res

@router.get("/chart_detail" , auth=JWTAuth(), response=ChartModelItems_out)
def list(request, chart_uuid : UUID4):
    a = Chart(request)
    res = a.GetChartDetail(chart_uuid)
    return  res

# Chart Type
@router.get("/charts_type_list" , auth=JWTAuth(), response=List[ChartTypeModelItems_out])
def list(request):
    a = Chart(request)
    res = a.GetChartTypeList()
    host = request.META['HTTP_HOST']
    return  res

# Layout
@router.post("/add_layout", auth=JWTAuth())
def create(request,LayoutModelItems: LayoutModelItems = Form(...)):
    a = Chart(request)
    b = a.addNewLayout(LayoutModelItems)
    return {"res":LayoutModelItems}