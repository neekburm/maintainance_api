import requests
import json

class EdmundsAPI:
    BASE_URL =  "https://api.edmunds.com/"
    API_KEY = "gm2gxxwnrw7yca8xp4s754rf"
    API_SECRET = "syA6hKQ5U7WVMD7BDqewgYTu"

    def __init__(self, key=API_KEY):
        self._parameters = {'api_key': key, 'fmt': 'json'}

    def getMakes(self):
        endpoint = "api/vehicle/v2/makes?"
        payload = self._parameters
        response = requests.get(self.BASE_URL + endpoint, params=payload)
        result = []
        for make in response.json()["makes"]:
            result.append("name": make["name"], "niceName": make["niceName"])
        return result

    def getID(self, make, model, year):
        endpoint = "api/vehicle/v2/" + make + "/" + model + "/" + year + "?"
        payload = self._parameters
        response = requests.get(self.BASE_URL + endpoint, params=payload)
        return response.json()["id"]

    def getModels(self, make):
        endpoint = "api/vehicle/v2/" + make + "/models?"
        payload = self._parameters
        response = requests.get(self.BASE_URL + endpoint, params=payload).json()
        result = []
        for model in response["models"]:
            result.append("name": model["name"], "niceName": model["niceName"])
        return response

    def getMaintenanceSchedule(self, model_year_id):
        endpoint = "v1/api/maintenance/actionrepository/findbymodelyearid?"
        payload = self._parameters
        payload["modelyearid"] = model_year_id
        response = requests.get(self.BASE_URL + endpoint, params=payload)
        return response.json()
