from peewee import *

# Sqlite
DATABASE = "mydatabase.db"
database = SqliteDatabase(DATABASE)

# Mysql
# DATABASE = "mydatabase"
# database = MySQLDatabase(database=DATABASE,user="root",passwd="") 

class BaseModel(Model):
    class Meta:
        database = database