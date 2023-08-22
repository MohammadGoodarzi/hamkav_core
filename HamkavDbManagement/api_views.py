from django.shortcuts import get_object_or_404
from .models import DataBaseConnectionModel, DataBaseType, DataSourceModel
from HamkavAuth.models import User
from . execSqlQuery import execPgQuery


from ninja_jwt.authentication import JWTAuth # jwt

class DB:  # کلاس عملیات با کانکشنهای دیتابیس
    def __init__(self, request):
        # print(self.request.user)
        # self.dbCconnectionItems = dbCconnectionItems
        self.request = request
        pass
        
    def addNewConnection(self, dbConnectionItems):
        
        databasetype = get_object_or_404(DataBaseType,uuid = dbConnectionItems.database_type_uuid )
        
        # user = User.objects.get(phone_number = '09158110553')
        # print(request.user)
        res = DataBaseConnectionModel.objects.create(
            user_creator = self.request.user,
            database_type=databasetype,
            url = dbConnectionItems.url,
            title = dbConnectionItems.title,
            name = dbConnectionItems.name,
            port = dbConnectionItems.port,
            username = dbConnectionItems.username,
            password = dbConnectionItems.password,
            connection_string = dbConnectionItems.connection_string,
            description = dbConnectionItems.description
        )
        return res
    
    def addNewDatasource(self, datasourceItems):
        
        databaseConnection = get_object_or_404( DataBaseConnectionModel,uuid = datasourceItems.database_connection_uuid )

        res = DataSourceModel.objects.create(
            user_creator = self.request.user,
            database_connection=databaseConnection,
            title = datasourceItems.title,
            query_string = datasourceItems.query_string,
            description = datasourceItems.description
        )
        return res
    
    def ConnectionList(self):
        res = DataBaseConnectionModel.objects.filter(is_active = True)
        # res = DataBaseConnectionModel.objects.all()
        # res = DataBaseConnectionModel.objects.select_related("database_type")
        return  list(res)
        
    def  DatasourceList(self):
        # res = DataBaseConnectionModel.objects.filter(is_active = True)
        # res = DataBaseConnectionModel.objects.all()
        res = DataSourceModel.objects.select_related("database_connection")
        return  list(res)
    
    def RunQuery(self):
        db_params = {
            "host": "localhost",
            "database": "mentolink",
            "user": "postgres",
            "password": "1234",
            'port': '5432',
        }
        query = "select * from sample_tbl limit 10;"
        
        a = execPgQuery(db_params=db_params, query=query)
        return a
    
    
    
    
    