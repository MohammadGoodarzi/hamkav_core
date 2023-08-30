from ninja import Router
from ninja_jwt.authentication import JWTAuth  # jwt
from ninja import NinjaAPI,Form,Schema
from typing import List
from pydantic import UUID4, Json


from .models import LayoutModel
from . api_views import Layout, Chart


router = Router()

class ChartModelItems(Schema):
    datasource_uuid: UUID4
    title:str
    description:str
    chart_type_id :int
    chart_type_title :str
    chart_base_config:Json = {}
    chart_access:str


@router.post("/add_chart", auth=JWTAuth())
def create(request,ChartModelItems: ChartModelItems = Form(...)):

    a = Chart(request)
    b = a.addNewChart(ChartModelItems)
    return {"res":ChartModelItems}