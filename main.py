from flask import Flask, render_template, jsonify
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import SelectField, SubmitField
from edmundsAPI import EdmundsAPI
app = Flask(__name__)
bootstrap = Bootstrap(app)

edmunds = EdmundsAPI()

@app.route('/_get_makes')
def getMakes():
	return jsonify(result=edmunds.getMakes())

@app.route('/_get_models/<make>')
def getModels(make):
	return jsonify(result=edmunds.getModels(make))

@app.route('/_get_id/<make>/<model>/<year>')
def getID(make, model, year):
	return jsonify(result=edmunds.getID(make, model, year))

@app.route('/_get_maintenance_schedule/<id>')
def getMaintenanceSchedule(id):
	return jsonify(result=edmunds.getMaintenanceSchedule(id))  

@app.route('/', methods=['GET', 'POST'])
def index():
	make_list = edmunds.getMakes()
	return render_template('index.html', make_list=make_list)

if __name__ == '__main__':
	app.run(debug=True)
