from Ishadowsocks import Ishadowsocks

if __name__=="__main__":
    print "SSAccountLoad----main----in-----"
    accountsList = []
    socksSource = Ishadowsocks()
    accountsList = socksSource.update()
    print "SSAccountLoad----main----out-----"
