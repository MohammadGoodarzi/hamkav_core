from django.shortcuts import get_object_or_404
from .models import DataBaseConnectionModel, DataBaseType, DataSourceModel
from HamkavAuth.models import User
from . execSqlQuery import execPgQuery
from django.shortcuts import get_object_or_404 

from HamkavConfigurator.models import Category_type2
from HamkavConfigurator.api_views import get_category_hierarchy_in_model_relation


from ninja_jwt.authentication import JWTAuth # jwt

class DB:  # کلاس عملیات با کانکشنهای دیتابیس
    def __init__(self, request):
        # print(self.request.user)
        # self.dbCconnectionItems = dbCconnectionItems
        self.request = request
        
        
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
        cat = get_object_or_404(Category_type2,id =datasourceItems.category) 
        


        if datasourceItems.uuid:
            # obj = get_object_or_404(DataSourceModel, uuid = datasourceItems.uuid)
            obj = DataSourceModel.objects.filter(uuid = datasourceItems.uuid) 
            res = obj.update(
                user_creator = self.request.user,
                database_connection=databaseConnection,
                title = datasourceItems.title,
                query_string = datasourceItems.query_string,
                description = datasourceItems.description,
                category = cat
            )
        else:
            res = DataSourceModel.objects.create(
                user_creator = self.request.user,
                database_connection=databaseConnection,
                title = datasourceItems.title,
                query_string = datasourceItems.query_string,
                description = datasourceItems.description,
                category = cat
             )
        
      
                
        # obj, created = DataSourceModel.objects.get_or_create(
                    # uuid = datasourceItems.uuid ,
                    #         defaults={
                    #                 'user_creator': self.request.user,
                    #                 'database_connection':databaseConnection,
                    #                 'title': datasourceItems.title,
                    #                 'query_string': datasourceItems.query_string,
                    #                 'description': datasourceItems.description,
                    #                 'category': cat
                    #         }
                            
                            
                            # )
        
        
        
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
    
    def RunQuery(self,sqlQueryText):
        # db_params = {
        #     "host": "localhost",
        #     "database": "mentolink",
        #     "user": "postgres",
        #     "password": "1234",
        #     'port': '5432',
        # }
        
        db_params = {}
             
        # query = "   select * from sample_tbl limit 100;   "
        params = get_object_or_404(DataBaseConnectionModel, uuid = sqlQueryText.database_connection_uuid)
        
        # db_params["host"] =  params.url
        # db_params["database"] =  params.name
        # db_params["user"] =  params.username
        # db_params["password"] =  params.password
        # db_params["port"] =  params.port
        
        # print("database_connection_uuid",sqlQueryText.database_connection_uuid)
        # a = execPgQuery(db_params=db_params, query=sqlQueryText.query_string)
        a = run_sql(params,sqlQueryText.query_string)
        return a
    
    def GetDataSourceResult(self, datasource_uuid):
        # print("datasource_uuid",datasource_uuid)
        # params= DataSourceModel.objects.get(uuid = datasource_uuid)
        # params2 = params.database_connection
        # print("params2",params2)
        m1 = get_object_or_404(DataSourceModel, uuid = datasource_uuid) 
        query_string = m1.query_string
        params = m1.database_connection
        return run_sql(params,query_string)  
    
    def GetCategorisedDataSourceList(self):
   
        root_categories = Category_type2.get_root_nodes()
        # print(root_categories)
        category_hierarchy_json = [get_category_hierarchy_in_model_relation(category, 'datasource_category', 'pi pi-folder', 'pi pi-th-large') for category in root_categories]
        return  category_hierarchy_json
    
    def GetDataSourceDetails(self, datasource_uuid):
        res = get_object_or_404(DataSourceModel, uuid = datasource_uuid)
        
        return res

         
    
def run_sql(params,query_string):
        db_params = {}
        
        db_params["host"] =  params.url
        db_params["database"] =  params.name
        db_params["user"] =  params.username
        db_params["password"] =  params.password
        db_params["port"] =  params.port
        
        # print("database_connection_uuid",sqlQueryText.database_connection_uuid)
        a = execPgQuery(db_params=db_params, query=query_string)
        return a    
    
    
    