from peewee import *
conexion=MySQLDatabase(database='#nombreDeBase',user='root',password='admin',port=3306,host='localhost')

class User(Model):
    username=CharField(max_length=10,unique=True)
    password=CharField(max_length=10)
    class Meta():
        database=conexion
        table_name='Users'
