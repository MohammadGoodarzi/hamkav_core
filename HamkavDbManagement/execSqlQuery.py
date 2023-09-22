from django.db import connection
import cx_Oracle
import psycopg2
import psycopg2.extras

# # Execute the query
# with connection.cursor() as cursor:
#     cursor.execute("sql_query")
#     results = cursor.fetchall()
   
def execPgQuery(db_params, query):    

    connection = psycopg2.connect(**db_params)

    # Create a cursor
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    # Execute a query
    cursor.execute(query)
    
    # print(cursor.description)
    column_names = [desc[0] for desc in cursor.description]
   

    # Fetch the results
    results = cursor.fetchall()
    # results = [dict(row) for row in cursor.fetchall()]

    # # Print the results
    # for row in results:
    #     print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return {"column_names": column_names, "query_result": results}


# # import pyodbc 




# #---------------------------------
# def getConnection(source):
#     # if source=='ERP':
#     #     ERPconn="Driver={SQL Server Native Client 11.0};Server=SRV-BI1\SQL2017DEF; Database=ERP;uid=mislogin;pwd=sharepoint;Trusted_connection=no;"
#     #     return ERPconn
#     if source=='ERP':
#         ERPconn="Driver={SQL Server Native Client 11.0};Server=172.16.0.144\SQL2014DEF; Database=ERP;uid=user_bi;pwd=@1475Temp2!;Trusted_connection=no;"
#         return ERPconn
#     if source=='DataWarehouse':
#         DWconn="Driver={SQL Server Native Client 11.0};Server=SRV-BI1\SQL2017DEF; Database=DataWarehouse;uid=mislogin;pwd=sharepoint;Trusted_Connection=yes;"
#         return DWconn
#     if source=='DataWarehouse_laptop':
#         DWlaptopconn="Driver={SQL Server Native Client 11.0};Server=WIN-O860UGRLNOQ\SQL2017DEF; Database=DataWarehouse;uid=mislogin;pwd=sharePoint;Trusted_Connection=yes;"
#         return DWlaptopconn
#     else:
#         None    

# #---------------------------------
# def select_data_mssql(conn,query):
#     conn = pyodbc.connect(conn)

#     cursor = conn.cursor()
#     cursor.execute(query)

#     # cursor.execute("select user_name from users where user_id=?", userid)
#     # row = cursor.fetchone()
#     # if row:
#     #     print(row.user_name)

    
#     # for row in cursor:
#     #     a=row
    

#     row = cursor.fetchone()
#     return row
#     # return row.id
# #---------------------------------
# #---------------------------------
# def select_data_mssql_fetchall(conn,query):
#     conn = pyodbc.connect(conn)

#     cursor = conn.cursor()
#     cursor.execute(query)

#     # cursor.execute("select user_name from users where user_id=?", userid)
#     # row = cursor.fetchone()
#     # if row:
#     #     print(row.user_name)

    
#     # for row in cursor:
#     #     a=row
    

#     row = cursor.fetchall()
#     return row
#     # return row.id
# #---------------------------------






# # import pyodbc 

# # def getdata
# # conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=SRV-BI1\SQL2017DEF; Database=DataWarehouse;uid=mislogin;pwd=sharepoint;Trusted_Connection=yes;")

# # cursor = conn.cursor()
# # cursor.execute('select * from employe.FactPersonal')

# # for row in cursor:
# #     print(row)


