# Global imports
import requests
from bs4 import BeautifulSoup
from random import choice

# Local imports
from firebaseinit import  Firebase


fire = Firebase()


class Scraper:
    user_agents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
        'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
    ]
    
    def fetch(self, URL):
        data = {}
        used = []

        Flag0 = False
        while not Flag0:
            user_agent = choice(self.user_agents)

            if len(used) != len(self.user_agents):
                if user_agent not in used:
                    used.append(user_agent)

                    HEADERS = ({
                        'User-Agent': user_agent,
                        'Accept-Language': 'en-US, en;q=0.5'
                    })

                    try:
                        webpage = requests.get(URL, headers=HEADERS)
                        code = BeautifulSoup(webpage.content, 'html.parser')
                    
                        if 'www.amazon.in' in URL:
                            try:
                                try:
                                    try:
                                        prices = code.select('.apexPriceToPay span')
                                        price = float(prices[0].get_text()[1:].replace(',', ''))

                                    except:
                                        prices = code.select('#corePriceDisplay_desktop_feature_div .a-price-whole')
                                        price = float(prices[0].get_text().replace(',', ''))

                                except:
                                    price = 'Out of stock.'

                                names = code.select('#productTitle')
                                name = names[-1].get_text().strip()
                                
                                page = str(URL).split('.')[1]
                                
                                dataset = {page: {'url': URL, 'name': name, 'price': price}}
                                data.update(dataset)

                                Flag0 = True

                            except:
                                continue
                        
                        elif 'www.flipkart.com' in URL:
                            try:
                                try: 
                                    prices = code.select('._16FRp0')
                                    price = prices[0].get_text()

                                    if price == 'Sold Out':
                                        price = 'Out of stock.'

                                except:
                                    try:
                                        prices = code.select('._16Jk6d')
                                        price = float(prices[0].get_text()[1:].replace(',', ''))

                                    except:
                                        price = 'Out of stock.'

                                names = code.select('.B_NuCI')
                                name = names[-1].get_text().strip()

                                page = str(URL).split('.')[1]

                                dataset = {page: {'url': URL, 'name': name, 'price': price}}
                                data.update(dataset)

                                Flag0 = True

                            except:
                                continue

                    except:
                        print("\nOuterError.\n")

            else:
                return "Failed."

        try:
            return data

        except:
            return "\nRetrieval failed.\n"

if __name__ == '__main__':
    urls = [
        'https://www.amazon.in/Lenovo-39-62cm-Windows-Keyboard-82JW0052IN/dp/B09DMWJH96/ref=sr_1_3?keywords=Lenovo+legion+5+5800h&qid=1639501786&sr=8-3',
        'https://www.flipkart.com/lenovo-legion-5-ryzen-7-octa-core-5800h-16-gb-512-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-rtx-3050-15ach6-gaming-laptop/p/itm50d5ba7a10251?pid=COMG62ZASBMGDC5M&lid=LSTCOMG62ZASBMGDC5MRQSUJN&marketplace=FLIPKART&q=lenovo+legion&store=search.flipkart.com&srno=s_1_5&otracker=search&otracker1=search&fm=SEARCH&iid=ba962896-dbc7-474c-b6fa-3bae3dce1c8f.COMG62ZASBMGDC5M.SEARCH&ppt=sp&ppn=sp&ssid=a4i46g498g0000001639500094619&qH=5dc4906269c2c6e5'
    ]
    scrape = Scraper()
    #print(scrape.monitor(urls))

    URL = 'https://www.amazon.in/Lenovo-39-62cm-Windows-Keyboard-82JW0052IN/dp/B09DMWJH96/ref=sr_1_3?keywords=Lenovo+legion+5+5800h&qid=1639501786&sr=8-3'
    print(scrape.fetch(URL))


# thriftypricechecker@gmail.com, igotthemkeyskeyskeys