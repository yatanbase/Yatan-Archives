#error

#first import connector
import mysql.connector

db= mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password= "qwerty123",
    database= "pythondb"

)

#create cursor now

mycursor = db.cursor()

studentRecord = """CREATE TABLE STUDENT ( 
                   NAME  VARCHAR(20) NOT NULL, 
                   BRANCH VARCHAR(50), 
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5), 
                   AGE INT
                   )"""

# table created
z="""insert into student 
    values("yta","cs",2,"cs","csd32",18)"""
mycursor.execute(z)
for i in mycursor:
    print (i)



print("hiii")