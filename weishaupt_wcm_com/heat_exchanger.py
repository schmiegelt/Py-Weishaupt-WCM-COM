import requests
import json
from requests.auth import HTTPDigestAuth

ENDPOINT = "/parameter.json"
QUERYTELEGRAM = '{"prot":"coco","telegramm":[[10,0,1,3196,0,0,0,0],[10,0,1,3197,0,0,0,0],[10,0,1,3198,0,0,0,0],[10,0,1,3199,0,0,0,0],[10,0,1,700,0,0,0,0],[10,0,1,3793,0,0,0,0],[10,0,1,3792,0,0,0,0],[0,0,1,5016,255,1,0,0],[0,0,1,5009,255,1,0,0]]}'


OILCONSUMTION_ID = 3793
OILCONSUMPTION_KEY = "Oil Consumption"

def process_values(server, username, password):
        req = requests.post(server + ENDPOINT, auth=HTTPDigestAuth(username, password), data=QUERYTELEGRAM)

        telegram = json.loads(req.text)['telegramm']
        result = {}
        for reading in telegram:
                if reading[3] == OILCONSUMTION_ID:
                        result[OILCONSUMPTION_KEY] = reading[6]
        return json.dumps(result)

