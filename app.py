# -*- coding: utf-8 -*-
from flask import Flask, Response, render_template, request
from flask_cors import CORS, cross_origin
from database.setting import session
from database.model.item import Item

class FlaskWithVuejs(Flask):
  jinja_options = Flask.jinja_options.copy()
  jinja_options.update(dict(
    block_start_string='(%',
    block_end_string='%)',
    variable_start_string='((',
    variable_end_string='))',
    comment_start_string='(#',
    comment_end_string='#)',
  ))

app = FlaskWithVuejs(__name__)
CORS(app)

api_path = '/api/1.0.0/'

@app.route(api_path + 'items')
def get_items():
    items = session.query(Item).all()
    result = '{"items":['

    for item in items:
        result += str(item) + ','
    else:
        result =result[:-1]

    result += ']}'

    response = Response(response=result,
                status=200,
                mimetype="application/json")

    return response

@app.route(api_path + 'item/<id>', methods=["GET"])
def get_item(id):
    item = session.query(Item).filter(Item.id==id).all()
    return item[0].__str__() if item else "{}"

@app.route(api_path + 'item/<id>', methods=["POST"])
def create_item(id):
    item = Item()
    item.id = id
    item.name = request.form['name']
    item.amount = int(request.form['amount'])
    session.add(item)
    session.commit()
    return str(item)

@app.route(api_path + 'item/<id>', methods=["DELETE"])
def delete_item(id):
    item = session.query(Item).filter(Item.id==id).delete()
    session.commit()
    return "success"

@app.route('/', methods=["GET"])
def index():
    return render_template('html/index.html')