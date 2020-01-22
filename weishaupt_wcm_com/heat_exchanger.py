import requests
import json
from requests.auth import HTTPDigestAuth

ENDPOINT = "/parameter.json"
QUERYTELEGRAM = (
    '{"prot":"coco","telegramm":[[10,0,1,3793,0,0,0,0],[10,0,1,12,0,0,0,0]]}'
)

VALUE = 1
TEMP = 2

# ID, Name, Value/Temp
QUERIES = [[3793, "Oil Meter", VALUE], [12, "Outside Temperature", TEMP]]



def getTemperture(lowByte, highByte):
    return (lowByte + 265 * highByte) / 10


def getValue(lowByte, highByte):
    return lowByte + 265 * highByte


def process_values(server, username, password):
    try:
        req = requests.post(
            "http://" + server + ENDPOINT,
            auth=HTTPDigestAuth(username, password),
            data=QUERYTELEGRAM,
        )
        telegram = json.loads(req.text)["telegramm"]
        result = {}
        for message in telegram:
            for reading in QUERIES:
                print(reading)
                if message[3] == reading[0]:
                    if reading[2] == TEMP:
                        result[reading[1]] = getTemperture(message[6], message[7])
                    else:
                        result[reading[1]] = getValue(message[6], message[7])
        return json.dumps(result)
    except:
        print("Error getting readings")
        return None

