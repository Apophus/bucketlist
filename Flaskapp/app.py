#!usr/bin/python

#create the application instance
from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__) #Flask will use this to determine root path of the app so it can find resource files relative to the app
app.config.from_object('config')

#database

mysql = MySQL()

#mysql conigurations
app.config['MYSQL_DATABASE_USER'] ='larrisa'
app.config['MYSQL_DATABASE_PASSWORD']= 'hkilel07'
app.config['MYSQL_DATABASE_DB'] = 'Bucketlist'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
#db is the database
#db = SQLAlchemy(app)

#from app import views,models
from flask import Flask, render_template,request, json #as the name suggests, we use it to render our template
#define basic route and it's corresponding request handler
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    #read posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    #validate the received values
    if _name and _email and _password:

        #call the database first
        conn = mysql.connect()
        cursor = conn.cursor()
        _hashed_password = generate_password_hash(_password)
        cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
        data = cursor.fetchall()

        if len(data) is 0:
            conn.commit()
            return json.dumps({'message':'User created successfully'})
        else:
            return json.dumps({'error':str(data[0])})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

except Exception as e:
    return json.dumps({'error':str(e)})
finally:
    cusor.close()
    conn.close()
    #return render_template('signup.html')






#checks if the executed file is the main program and runs the app
if __name__ == "__main__":
    app.run(debug=True)


