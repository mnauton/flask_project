import mysql.connector
from mysql.connector import Error

from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['ENV'] = "Development"
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return 'hello test'

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run()


@app.route('/signupAction', methods=['POST'])
def signupAction():
    username = request.form.get("username")
    password = request.form.get("password")
    bio = request.form.get("bio")
    print(username, password, bio)
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             port='7703',
                                             database='MYDB',
                                             user='root',
                                             password='mypassword')
        if connection.is_connected():
            myquery = "INSERT INTO USER (Username,Password,Bio) VALUES ('" \
                      + username + "','" + password + "','" + bio + "');"
            cursor = connection.cursor()
            result = cursor.execute(myquery)
            connection.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return render_template("home.html")
