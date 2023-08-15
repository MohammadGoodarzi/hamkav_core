from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI,Form,Schema

api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}

class AddNewConnection(Schema):
    database_type: str
    url: str 
    title: str 
    name: str 
    port: int 
    username: str 
    password: str 
    connection_string: str  = None
    description: str  = None
    
@api.post("/AddNewConnection")
def create(request,addnewconnection: AddNewConnection = Form(...)):
    # return addnewconnection
    return {"res":addnewconnection,"ddd":"eeeeee"}

@api.post("/login2")
def login(request, username: str = Form(...), password: str = Form(...) ):
    return {'username': username, 'password': '*****'}

app_name = 'HamkavDbManagement'

urlpatterns = [
    
    path("api/", api.urls),
]