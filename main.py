from flask import Flask, render_template, jsonify
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import SelectField, SubmitField
from edmundsAPI import EdmundsAPI
app = Flask(__name__)
bootstrap = Bootstrap(app)

edmunds = EdmundsAPI()

@app.route('/_get_models/<make>')
def getModels(make):
	return jsonify(result=edmunds.getModels(make)) 

@app.route('/', methods=['GET', 'POST'])
def index():
	make_list = edmunds.getMakes()
	return render_template('index.html', make_list=make_list)

if __name__ == '__main__':
	app.run(debug=True)
