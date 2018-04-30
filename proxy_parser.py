#Despite on coding telegram_feeder in function coding style,
#I dicided to try OOP style to practice OOP skills, so this module
#has code programming style distinctions
import requests
from bs4 import BeautifulSoup


class Proxy():
    #Create Proxy class
    availible_proxy_site_url = 'https://www.ip-adress.com/proxy-list'

    def __init__(self):
        try:
            responce = requests.get(self.availible_proxy_site_url)
            self.html = responce.text
        except requests.exceptions.RequestException as e:
            print('Exception after get proxy happend: ', e)

    def get_availible_proxy_address(self):
        bs = BeautifulSoup(self.html, 'html.parser')
        for item in bs.find_all('td'):
            if '.' in item.text:
                proxy_ip = item.text
                proxies = dict(http='http://' + proxy_ip, https='https://'+ proxy_ip)
                url = 'http://ya.ru'
                try:
                    print('Trying proxy ' + proxy_ip)
                    responce = requests.get(url, proxies=proxies, timeout=1)
                    if responce.status_code == 200:
                        return proxies
                except requests.exceptions.RequestException as e:
                    print('Connection error')
                    continue


if __name__ == '__main__':
    proxy = Proxy()
    proxies = proxy.get_availible_proxy_address()
    print(proxies)
    url = 'https://ipinfo.info/html/ip_checker.php'
    r = requests.get(url, proxies=proxies)
    print(r.content)
