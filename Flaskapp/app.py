#!usr/bin/python

#create the application instance
from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__) #Flask will use this to determine root path of the app so it can find resource files relative to the app
app.config.from_object('config')
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
        return json.dumps({'html':'<span> All Fields good!!>/span>'})
    else: 
        return json.dumps({'html':'<span> Enter the required fields. </span>'})
    #return render_template('signup.html')

#checks if the executed file is the main program and runs the app
if __name__ == "__main__":
    app.run(debug=True)


