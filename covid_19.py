import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get('https://covid-19-statistics.p.rapidapi.com/regions')
    data = r.json()
    text = f'Confirmed Cases: {data["cases"]}\nDeaths :{data["deaths"]} \nRecovery:{data["recovered"]}'
    
    while True:
        toast = ToastNotifier()
        toast.show_toast("covid-19 updates", text, duration=20)
        time.sleep(60)

update()
   