from flask import Flask, render_template, jsonify, request, Response
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import SelectField, SubmitField
from edmundsAPI import EdmundsAPI
import json
app = Flask(__name__, static_url_path='', static_folder='static')
bootstrap = Bootstrap(app)

edmunds = EdmundsAPI()

@app.route('/_get_makes')
def getMakes():
	return Response(json.dumps(edmunds.getMakes()), mimetype='application/json', headers={'Cache-Control': 'no-cache'})

@app.route('/_get_models/<make>')
def getModels(make):
	return Response(json.dumps(edmunds.getModels(make)), mimetype='application/json', headers={'Cache-Control': 'no-cache'})

@app.route('/_get_id/<make>/<model>/<year>')
def getID(make, model, year):
	return jsonify(result=edmunds.getID(make, model, year))

@app.route('/_get_maintenance_schedule/<id>')
def getMaintenanceSchedule(id):
	return jsonify(result=edmunds.getMaintenanceSchedule(id))

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
