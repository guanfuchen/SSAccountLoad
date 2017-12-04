import requests
from bs4 import BeautifulSoup
from ShadowsocksAccount import ShadowsocksAccount
from fake_useragent import UserAgent

class GoIshadowsocks:
    def __str__(self):
        return "GoIshadowsocks"
    def __init__(self):
        print "GoIshadowsocks----init----in----"
        print "GoIshadowsocks----init----out----"
    def update(self):
        ua = UserAgent()
        # print(ua.chrome)
        header = {'User-Agent': str(ua.chrome)}
        url = "https://go.ishadowx.net/"
        html = requests.get(url, headers=header)

        html_content = html.content
        # html_content = open('GoIshadowsocks.html', 'r').read()
        soup = BeautifulSoup(html_content, "html.parser")
        freeInfos = soup.findAll("div", { "class" : "hover-text" })
        # print len(freeInfos)
        shadowsocksAccountsList = []
        for i in range(len(freeInfos)):
            # print i
            freeInfo = freeInfos[i]
            # print(freeInfo)
            h4_tags = freeInfo.findAll("h4")
            for h4_tag in h4_tags:
                # print h4_tag
                h4_tag_text = h4_tag.text
                if h4_tag_text.find('IP Address:') != -1:
                    ip_span = h4_tag.findAll("span")[0]
                    ip_span_text = ip_span.text.strip()
                    # print(ip_span_text)
                elif h4_tag_text.find('Port:') != -1:
                    port_span = h4_tag.findAll("span")[0]
                    port_span_text = port_span.text.strip()
                    # print(port_span_text)
                elif h4_tag_text.find('Password:') != -1:
                    password_span = h4_tag.findAll("span")[0]
                    password_span_text = password_span.text.strip()
                    # print(password_span_text)
                elif h4_tag_text.find('Method:') != -1:
                    method_text = h4_tag_text.split(':')[1].strip()
                    # print(method_text)
            account = ShadowsocksAccount()
            account.server = ip_span_text
            account.port = port_span_text
            account.passwd = password_span_text
            account.lockMethod = method_text
            print account
            shadowsocksAccountsList.append(account)
        return shadowsocksAccountsList

if __name__=="__main__":
    print "GoIshadowsocks----main----in----"
    shadow = GoIshadowsocks()
    shadow.update()
    print "GoIshadowsocks----main----out----"
