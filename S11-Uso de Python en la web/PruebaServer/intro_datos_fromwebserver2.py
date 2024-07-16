# from http.server import BaseHTTPRequestHandler, HTTPServer
# from mysql.connector import Error
# import mysql.connector


# class Database():
#     def connect_db(self):
#         try:
#             import mysql.connector
#             connex = mysql.connector.connect(
#             user="root", 
#             password="",
#             host="localhost",
#             database="datadb")
#             if connex.is_connected():
#                 return connex
#         except Error as e:
#             print("Error en MySQL: " + str(e))
        
#         finally:
#             print("Conexión a MySQL correcta")
    
#     def createTable(self):
#         cursor = self.connex.cursor()
#         cursor.execute("drop database if exists test")
#         cursor.execute("create database test")
#         cursor.execute("use test")
#         cursor.execute("create table datos(id int primary key auto_increment, mensaje varchar(255))")
#         cursor.close()
        
#     def insertData(self):
        
        
        
        
            
    # def insertarDato(data):
    #     connex = Database.connect_db()
    #     cursor = connex.cursor()
    #     cursor.execute( "INSERT INTO datos VALUES (NULL, %s,%s)", (data["Nombre"],data["Apellido"])) #NO OLVIDAR LA COMA
    #     connex.commit()
    #     cursor.close()
    #     connex.close()
        