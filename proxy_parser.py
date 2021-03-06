#Despite on coding telegram_feeder in function coding style,
#I dicided to try OOP style to practice OOP skills, so this module
#has code programming style distinctions
import requests
from bs4 import BeautifulSoup


USE_PROXY = False


class Proxy:
    #Create Proxy class
    availible_proxy_site_url = 'https://www.ip-adress.com/proxy-list'

    def __init__(self):
        if USE_PROXY:
            try:
                response = requests.get(self.availible_proxy_site_url)
                self.html = response.text
            except requests.exceptions.RequestException as e:
                self.html = None
                print('Exception after get proxy happend: ', e)

    def get_availible_proxy_address(self):
        if USE_PROXY:
            """Method retruns availible proxy ip address"""
            if self.html is not None:

                bs = BeautifulSoup(self.html, 'html.parser')
                proxy_ip_list = []
                for item in bs.find_all('td'):
                    if '.' in item.text:
                        proxy_ip_list.append(item.text)

                #Find availible proxy ip in proxy_ip_list
                for proxy_ip in proxy_ip_list:
                    proxies = dict(http='http://' + proxy_ip, https='https://'+ proxy_ip)
                    url = 'http://ya.ru'
                    try:
                        print('Trying proxy ' + proxy_ip)
                        response = requests.get(url, proxies=proxies, timeout=1)
                        if response.status_code == 200:
                            print('Found availible proxy ' + proxy_ip)
                            return proxies
                    except requests.exceptions.RequestException as e:
                        print('Proxy connection error')
                        continue
            else:
                return None
        else:
            return None


if __name__ == '__main__':
    proxy = Proxy()
    proxies = proxy.get_availible_proxy_address()
    print(proxies)
    url = 'https://ipinfo.info/html/ip_checker.php'
    r = requests.get(url, proxies=proxies)
    print(r.status_code)
