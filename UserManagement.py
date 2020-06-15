import mysql.connector

def getConnection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "usermanagement"
    )
    return db

def create(firstname,lastname,username,password,email):
    db = getConnection()
    mycursor = db.cursor()
    q = "insert into users(Firstname,Lastname,Username,Password,Email) values(%s,%s,%s,%s,%s)"
    
    mycursor.execute(q,(firstname,lastname,username,password,email))
    db.commit()
    db.close
    
def readAll():
    db = getConnection()
    mycursor = db.cursor()

    mycursor.execute("select * from users")
    for x in mycursor:
        print(x)
    db.close()

def read(col,val):
    db = getConnection()
    mycursor = db.cursor()

    q = "select * from users where {} = %s".format(col)
    mycursor.execute(q,(val,))
    for x in mycursor:
        print(x)
    db.close()

def deleteUser(uname):
    db = getConnection()
    mycursor = db.cursor()
    q = "delete from users where username = %s"
    
    mycursor.execute(q,(uname,))
    db.commit()
    db.close()
    
    
def delete(col,val):
    db = getConnection()
    mycursor = db.cursor()
    q = "delete from users where {} = %s".format(col)

    mycursor.execute(q,(val,))
    db.commit()
    db.close()

def updateAll(uname,firstname,lastname,username,password,email):
    db = getConnection()
    mycursor = db.cursor()
    q = "Update users set firstname = %s,lastname = %s,username = %s ,password = %s,email= %s where username = %s"

    mycursor.execute(q,(firstname,lastname,username,password,email,uname))
    db.commit()
    db.close()

def update(uname,col,val):
    db = getConnection()
    mycursor = db.cursor()
    q = "Update users set {} = %s where username = %s".format(col)

    mycursor.execute(q,(val,uname))
    db.commit()
    db.close()



