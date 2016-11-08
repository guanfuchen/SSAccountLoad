from SSQRDecode import SSQRDecode
import requests
from bs4 import BeautifulSoup

class Shadowsocks8:
    def __str__(self):
        return "Shadowsocks8"
    def __init__(self):
        print "Shadowsocks8----init----in----"
        print "Shadowsocks8----init----out----"
    def update(self):
        url = "http://www.shadowsocks8.net/"
        html = requests.get(url)
        html_content = html.content
        soup = BeautifulSoup(html_content, "html.parser")
        freeInfo = soup.select("img")
        shadowsocksAccountsList = []
        for i in range(3):
            print i
            #print freeInfo[1]
            accountUrl = url + freeInfo[2*i + 1].attrs['src']
            #print accountUrl
            account = SSQRDecode.decode(accountUrl)
            print account
            shadowsocksAccountsList.append(account)


if __name__=="__main__":
    print "Shadowsocks8----main----in----"
    mShadowsocks8 = Shadowsocks8()
    mShadowsocks8.update()
    print "Shadowsocks8----main----out----"
