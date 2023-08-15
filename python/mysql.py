#error

#first import connector
import _mysql_connector

db= _mysql_connector.connect(
    host="localhost",
    user="root",
    password= "qwerty123"
)

#create cursor now

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE pythondb")