import requests
import datetime
from http import HTTPStatus
from twilio.rest import Client
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    def send_alert():
        account_sid = "ACc59a4cd33a553e9d4994e6ae7584de2a"
        auth_token = "013efb82da7654ddd0852340dc816fdb"
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            url="https://raw.githubusercontent.com/SakethMadishetty/ML-Datasets/main/voice.xml",
            to="+19452674499",
            from_="+18557173142"
        )
        print(call.sid)
        return call.sid

    """Example Hello World route."""
    url = "https://publicapi.txdpsscheduler.com/api/AvailableLocation"
    phone_numbers = []
    payload = "{\"TypeId\":71,\"ZipCode\":\"76227\",\"CityName\":\"\",\"PreferredDay\" : 0}"
    headers = {
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8',
      'Connection': 'keep-alive',
      'Content-Type': 'application/json;charset=UTF-8',
      'Origin': 'https://public.txdpsscheduler.com',
      'Referer': 'https://public.txdpsscheduler.com/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
      'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'Cookie': 'ARRAffinity=64ead312f45cf5dd16619c1c8a0e93545e50b8a24203efc7c5d072ec4f0ae634; ARRAffinitySameSite=64ead312f45cf5dd16619c1c8a0e93545e50b8a24203efc7c5d072ec4f0ae634'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == HTTPStatus.OK:
      json_obj = response.json()
      print(json_obj[0]['NextAvailableDate'])
      json_obj[0]['NextAvailableDate'] = '02/14/2024'
      if datetime.datetime.strptime(json_obj[0]['NextAvailableDate'],"%m/%d/%Y") < datetime.datetime.strptime("03/11/2024","%m/%d/%Y"):
        sid = send_alert()
        return f"Alert sent with call id - {sid}!"

    return "No slots"
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
