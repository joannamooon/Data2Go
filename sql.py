import mysql.connector
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL(app)
cursor = mysql.connect().cursor()
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_details = request.form
        firstName = user_details['firstName']
        lastName = user_details['lastName']
        birthday = user_details['birthday']
        address = user_details['address']
        numChild = user_details['numChild']
        income = user_details['income']
        housing = user_details['housing']
        restrictions = user_details['restrictions']
        cursor.execute('INSERT INTO users(firstName, lastName, birthday, address, numChild, income, housing, restrictions) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (firstName, lastName, birthday, address, numChild, income, housing, restrictions))
        mysql.connect().commit()
        cursor.close()
        return 'success'
    return 'failed'