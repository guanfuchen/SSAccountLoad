class ShadowsocksAccount:
    def __str__(self):
        #print "ShadowsocksAccount"
        print "ShadowsocksAccount"
        print "server=" + self.server
        print "port=" + self.port
        print "passwd=" + self.passwd
        print "lockMethod=" + self.lockMethod
        return "ShadowsocksAccount"
    def __init__(self):
        print "ShadowsocksAccount----init----in----"
        self.server = ""
        self.port = ""
        self.passwd = ""
        self.lockMethod = ""
        print "ShadowsocksAccount----init----out----"
