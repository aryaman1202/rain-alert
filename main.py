import requests
import os
from twilio.rest import Client
api_key = "d5b4e641b6441a269155c68af97ed85c"
phone_no = "+19035679129"
account_sid = 'AC2e2ac9eba28ced6036f0afa990246ed8'
auth_token = '5c379e6b56bf2d1099bb62be228c60f5'
url = "https://api.openweathermap.org/data/2.5/onecall?lat=27.1833&lon=78.0167&appid=d5b4e641b6441a269155c68af97ed85c"

param = {
    "exclude": "current,minutely,daily"
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall?lat=27.1833&lon=78.0167&appid=d5b4e641b6441a269155c68af97ed85c", params=param)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:15]

will_rain = False

for hours in weather_slice:
    condition_code = hours["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Hey Aryaman, it's your weather assistant. There's a high possibility that it might rain today.So do carry an umbrella☔ and stay safe",
            from_=phone_no,
            to='+917455817186'
        )
