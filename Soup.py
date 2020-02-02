import requests
from bs4 import BeautifulSoup


class Soup():
    def bitcoin(id):
        req = requests.get('https://www.coinbase.com/price/bitcoin')
        soup = BeautifulSoup(req.text, "lxml")
        i = 0
        price = ''
        for sub_heading in soup.find_all('span'):
            if i == 9:
                price = sub_heading.text
                break
            i+=1
        return price[3:]


