import requests
import datetime
from http import HTTPStatus
from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse
import os
from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def hello_world():
    def send_alert():
        account_sid = ""
        auth_token = ""
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            url="https://texas-dps-slots-notifier-ki33up2wnq-uc.a.run.app/download_xml",
            to="+19452674499",
            from_="+18557173142"
        )
        print(call.sid)
        return call.sid

    def get_latest_booking():
        url = 'https://publicapi.txdpsscheduler.com/api/Booking'
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
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"'
        }

        data = {
            'FirstName': 'Saketh',
            'LastName': 'Madishetty',
            'DateOfBirth': '12/07/1997',
            'LastFourDigitsSsn': '2245'
        }

        response = requests.post(url, headers=headers, json=data)

        if response.json():
            return response.json()[0]
        return None

    def hold_slot(slot_id):
        url = 'https://publicapi.txdpsscheduler.com/api/HoldSlot'

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://public.txdpsscheduler.com',
            'Referer': 'https://public.txdpsscheduler.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"'
        }

        data = {
            'SlotId': slot_id,
            'FirstName': 'Saketh',
            'LastName': 'Madishetty',
            'DateOfBirth': '12/07/1997',
            'Last4Ssn': '2245'
        }
        print(f'holding slot with payload {data}')
        response = requests.post(url, headers=headers, json=data)
        print(f'slot hole response - {response.json()}')
        return response.json()

    def reschedule_booking(booking_date_time):
        url = "https://publicapi.txdpsscheduler.com/api/RescheduleBooking"

        payload = {
            "CardNumber": "",
            "FirstName": "Saketh",
            "LastName": "Madishetty",
            "DateOfBirth": "12/07/1997",
            "Last4Ssn": "2245",
            "Email": "sakethm.97@gmail.com",
            "CellPhone": "",
            "HomePhone": "",
            "ServiceTypeId": 21,
            "BookingDateTime": booking_date_time,
            "BookingDuration": 20,
            "SpanishLanguage": "N",
            "SiteId": 113
        }

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
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'Cookie': 'ARRAffinity=3fd8de456c99c884b0950144b7431b1c0dd0c52d947730e29d6132fb48aaa899; ARRAffinitySameSite=3fd8de456c99c884b0950144b7431b1c0dd0c52d947730e29d6132fb48aaa899'
        }
        print(f'rescheduling  slot with payload {payload}')
        response = requests.post(url, headers=headers, json=payload)
        # response = requests.request("POST", url, headers=headers, data=payload)
        print(f'rescheduling  slot response- {response.text}')
        return response.text
    # get_latest_booking()
    # print(get_latest_booking())

    url = "https://publicapi.txdpsscheduler.com/api/AvailableLocation"

    payload = "{\"TypeId\":21,\"ZipCode\":\"76227\",\"CityName\":\"\",\"PreferredDay\" : 0}"
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
      latest_booking = get_latest_booking()
      # print(json_obj[0]['NextAvailableDate'],json_obj[0]['Name'])
      # json_obj[0]['NextAvailableDate'] = '02/14/2024'

      slot_id = json_obj[0]['Availability']['LocationAvailabilityDates'][0]['AvailableTimeSlots'][0]['SlotId']
      new_booking_date_time = json_obj[0]['Availability']['LocationAvailabilityDates'][0]['AvailableTimeSlots'][0]['StartDateTime']
      print(json_obj[0]['Name'], slot_id, new_booking_date_time)
      if (datetime.datetime.strptime(new_booking_date_time,"%Y-%m-%dT%H:%M:%S") <
              datetime.datetime.strptime(latest_booking['BookingDateTime'],"%Y-%m-%dT%H:%M:%S")):

        res1 = hold_slot(slot_id)
        if res1['SlotHeldSuccessfully']:
            res2 = reschedule_booking(new_booking_date_time)
            # print(res2['Booking'])
            return res2
        else:
            print(f'Slot hold failed for slot id {slot_id}')
        # sid = send_alert()
        # return f"Alert sent with call id - {sid}!"

    return "No slots"

@app.route('/download_xml',methods=['POST'])
def download_xml():
    response = VoiceResponse()
    response.say("Drivers license early slots available. Go book now.")
    # # Using TwiML to create a simple Voice Response with a Gather element
    # with response.gather(numDigits=1, action='/gather_response'):
    #     response.say("Press 1 to continue, or any other key to exit.")

    return Response(str(response), content_type='application/xml')
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
