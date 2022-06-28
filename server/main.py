from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
from flask import Flask
from flask import send_from_directory
from flask import render_template
import ast

app = Flask(__name__)
api = Api(app)

class DinDon(Resource):
    def get(self):
        pass;

@app.route('/')
def say_hello():
    return ('Hello world')

api.add_resource(DinDon, '/DinDon')

if __name__ == '__main__':
    app.run()