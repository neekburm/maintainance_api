import requests
import json
from edmundsAPI import EdmundsAPI


edmunds = EdmundsAPI()
make_list = edmunds.getMakes()

with open("edmunds_data/toyota_models.json", 'w') as fp:
    json.dump(edmunds.getModels("toyota"), fp, sort_keys=True, indent=4)

# with open("4runner_maintainence.json", "w") as fp:
#     json.dump(edmunds.getMaintainanceSchedule("591"), fp, sort_keys=True, indent=4)