import requests
import json
from edmundsAPI import EdmundsAPI


edmunds = EdmundsAPI()
make_list = edmunds.getMakes()
car_id = edmunds.getID('toyota', 'corolla', '2013')
with open("edmunds_data/toyota_maintenance.json", 'w') as fp:
    json.dump(edmunds.getMaintenanceSchedule(car_id), fp, sort_keys=True, indent=4)

