#!usr/bin/python

#create the application instance
from flask import Flask
app = Flask(__name__) #Flask will use this to determine root path of the app so it can find resource files relative to the app

#define basic route and it's corresponding request handler
@app.route('/')
def main():
    return "Welcome!"

#checks if the executed file is the main program and runs the app
if __name__ = "__main__":
    app.run()
