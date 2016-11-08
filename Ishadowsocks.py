import requests
from bs4 import BeautifulSoup
from ShadowsocksAccount import ShadowsocksAccount

class Ishadowsocks:
    def __str__(self):
        return "Ishadowsocks"
    def __init__(self):
        print "Ishadowsocks----init----in----"
        print "Ishadowsocks----init----out----"
    def update(self):
        url = "http://www.ishadowsocks.org/#free"
        html = requests.get(url)
        html_content = html.content
        soup = BeautifulSoup(html_content, "html.parser")
        freeInfo = soup.select("#free .col-sm-4 h4")
        #print len(freeInfo)
        shadowsocksAccountsList = []
        for i in range(3):
            print i
            account = ShadowsocksAccount()
            account.server = freeInfo[0 + 6*i].string.rsplit(':', 1)[-1]
            account.port = freeInfo[1 + 6*i].string.rsplit(':', 1)[-1]
            account.passwd = freeInfo[2 + 6*i].string.rsplit(':', 1)[-1]
            account.lockMethod = freeInfo[3 +6*i].string.rsplit(':', 1)[-1]
            print account
            shadowsocksAccountsList.append(account)
        return shadowsocksAccountsList




if __name__=="__main__":
    print "Ishadowsocks----main----in----"
    shadow = Ishadowsocks()
    shadow.update()
    print "Ishadowsocks----main----out----"
