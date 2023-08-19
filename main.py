import requests


name_city = ["Череповец", "Лондон", "SVO"] 

payload = {
    "m":"",
    "M":"",
    "q":"",
    "T":"",
    "n":"",
    "lang": "ru"
}

for i in range(3):  
    url = 'https://wttr.in/{city}'.format(city=name_city[i])
    response = requests.get(url,params=payload)
    response.raise_for_status()
    print(response.text)
