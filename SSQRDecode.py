from ShadowsocksAccount import ShadowsocksAccount
import requests
import json
import base64

class SSQRDecode:
    def __str__(self):
        return "SSQRDecode"
    def __init__(self):
        print "SSQRDecode----init----in----"
        print "SSQRDecode----init----out----"
    @classmethod
    def decode(cls, url):
        qrDecodeUrl = "http://api.qrserver.com/v1/read-qr-code/?fileurl="
        html = requests.get(qrDecodeUrl + url)
        html_content = html.content
        jsonObj = json.loads(html_content)
        #print jsonObj
        base64EncodeStr = jsonObj[0]['symbol'][0]['data'].rsplit('/', 1)[-1]
        #print base64EncodeStr
        base64DecodeStr = base64.b64decode(base64EncodeStr).strip()
        account = ShadowsocksAccount()
        splitStrList = base64DecodeStr.split(":", 1)
        account.lockMethod = splitStrList[0]
        splitStrList = splitStrList[1].split("@", 1)
        account.passwd = splitStrList[0]
        splitStrList = splitStrList[1].split(":", 1)
        account.server = splitStrList[0]
        account.port = splitStrList[1]
        #print account
        return account

if __name__=="__main__":
    print "SSQRDecode----main----in----"
    mSSQRDecode = SSQRDecode()
    url = "http://api.qrserver.com/v1/read-qr-code/?fileurl=http://www.shadowsocks8.net/images/server01.png"
    mSSQRDecode.decode(url)
    print "SSQRDecode----main----out----"
