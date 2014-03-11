'''

@author: it
'''
import urllib2
import urllib

class AutoLogin():
    '''
    classdocs
    '''


    def __init__(self, url, username, password):
        '''
        Constructor
        '''
        self.username_ = username
        self.password_ = password
        
    def login(self):
        postdata = urllib.urlencode({'username': self.username_,
                                     'password': self.password_,
                                     'pwd': self.password_,
                                     'secret':'true'
                                    })
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        req = urllib2.Request(url,
                              postdata,
                              headers
                              )
        
        try:
            fd = urllib2.urlopen(req)
            data = fd.read(1024)
            if not len(data):
                print data
            else:
                print 'No data'
        except urllib2.HTTPError, error:
            content = error.read()
            print 'Error: ' + content
            
autoLogin = AutoLogin('http://xxx.xxx.xxx.xxx', 'username', 'password').login()
