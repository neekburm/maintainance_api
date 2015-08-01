import requests
import json
from edmundsAPI import EdmundsAPI
from firebase import firebase
firebase = firebase.FirebaseApplication("https://maintenance-api.firebaseio.com/", None)
edmunds = EdmundsAPI()
makes = edmunds.getMakes()
firebase.post('/makes', makes)

for make in makes["makes"]:
	models = edmunds.getModels(make["niceName"])
	firebase.post('/models/' + )
