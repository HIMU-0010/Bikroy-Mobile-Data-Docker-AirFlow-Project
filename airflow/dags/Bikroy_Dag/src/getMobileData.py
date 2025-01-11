import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

def get_mobiles():
    url = "https://bikroy.com/bn/ads/bangladesh/mobiles"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    script = soup.find_all('script', type="application/ld+json")[0]
    mobiles = json.loads(script.string)['itemListElement']
    return mobiles

def process_mobiles():
    mobiles = get_mobiles()
    mobile_data = []
    for mobile in mobiles:
        mobile_data.append({
            'name': mobile['name'],
            'url': mobile['url'],
            'date_fetched': datetime.now().isoformat()
        })
    
    with open("mobile_data.json", "w") as f:
        json.dump( mobile_data, f)