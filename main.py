import requests


city_names = ["Череповец", "Лондон", "SVO"] 

payload = {
    "m":"",
    "M":"",
    "q":"",
    "T":"",
    "n":"",
    "lang": "ru"
}

for city in city_names:  
    url = 'https://wttr.in/{city}'.format(city=city_names[city])
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)
