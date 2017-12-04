from fake_useragent import UserAgent

from SSQRDecode import SSQRDecode
import requests
from bs4 import BeautifulSoup

class FreessCX:
    def __str__(self):
        return "FreessCX"
    def __init__(self):
        print "FreessCX----init----in----"
        print "FreessCX----init----out----"
    def update(self):
        ua = UserAgent()
        # print(ua.chrome)
        header = {'User-Agent': str(ua.chrome)}
        url = "https://freess.cx/"
        html = requests.get(url, headers=header)
        html_content = html.content
        soup = BeautifulSoup(html_content, "html.parser")
        freeInfos = soup.findAll('div', {'class': '4u 12u(mobile)'})
        shadowsocksAccountsList = []
        for i in range(len(freeInfos)):
            print i
            freeInfo = freeInfos[i]
            accountUrl = freeInfo.findAll('a')[0]['href']
            print accountUrl
            account = SSQRDecode.decode(url + accountUrl)
            print account
            shadowsocksAccountsList.append(account)

        return shadowsocksAccountsList


if __name__=="__main__":
    print "FreessCX----main----in----"
    shadow = FreessCX()
    shadow.update()
    print "FreessCX----main----out----"
