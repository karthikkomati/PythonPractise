import pymysql
from flask import Flask, jsonify,request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'UserManagement'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/getAll')
def getAll():

        mycursor = mysql.connect().cursor(pymysql.cursors.DictCursor)

        mycursor.execute("select * from users")
        rows=mycursor.fetchall()
        resp = jsonify(rows)
        return resp



@app.route('/get')
def get():
    try:
        mycursor = mysql.connect().cursor(pymysql.cursors.DictCursor)
        q = "select * from users where {} = %s".format(request.args.get('col'))
        mycursor.execute(q,(request.args.get('val'),))
        rows=mycursor.fetchall()
        resp = jsonify(rows)
        return resp
    except:
        print("error")

@app.route('/deleteUser')
def deleteUser():
    mycon = mysql.connect()
    mycursor = mycon.cursor(pymysql.cursors.DictCursor)
    q = "delete from users where username = %s"
    
    mycursor.execute(q,(request.args.get('username'),))
    mycon.commit()
    
    return getAll()

@app.route('/delete')
def delete():
    mycon = mysql.connect()
    mycursor = mycon.cursor(pymysql.cursors.DictCursor)
    q = "delete from users where {} = %s".format(request.args.get('col'))

    mycursor.execute(q,(request.args.get('val'),))
    mycon.commit()
    
    return getAll()

@app.route('/update')
def update():
    mycon = mysql.connect()
    mycursor = mycon.cursor(pymysql.cursors.DictCursor)
    q = "Update users set {} = %s where username = %s".format(request.args.get('col'))
    mycursor.execute(q,(request.args.get('val'),request.args.get('username')))
    mycon.commit()
    
    return getAll()

@app.route('/updateAll')
def updateAll():
    mycon = mysql.connect()
    mycursor = mycon.cursor(pymysql.cursors.DictCursor)
    q = "Update users set firstname = %s,lastname = %s,username = %s ,password = %s,email= %s where username = %s"
    mycursor.execute(q,(request.args.get('firstname'),request.args.get('lastname'),request.args.get('newusername'),request.args.get('password'),request.args.get('email'),request.args.get('username')))
    
    mycon.commit()
    
    return getAll()

@app.route('/create')
def create():
    mycon = mysql.connect()
    mycursor = mycon.cursor(pymysql.cursors.DictCursor)
    q = "insert into users(Firstname,Lastname,Username,Password,Email) values(%s,%s,%s,%s,%s)"
    mycursor.execute(q,(request.args.get('firstname'),request.args.get('lastname'),request.args.get('username'),request.args.get('password'),request.args.get('email')))
    mycon.commit()

    return getAll()

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def internal_error(error):

    return "Error: Invalid values entered"
    
    
    
if __name__ == '__main__':
    app.run()

