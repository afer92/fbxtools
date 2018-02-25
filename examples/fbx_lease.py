#!/usr/bin/env python

from fbxtools.utils import get_url_api
from fbxtools.fbx import Fbx

url_api = get_url_api()

print url_api

## Initialize and connect app.
app = Fbx('https://mafreebox.freebox.fr/api/v5', verify_cert=False)
#app = Fbx(url_api)
app.get_session_token()

def main():
    stls = app.staticleases
    #print(u'stls:',stls)
    for sl in stls:
        print(u'+++')
        print(u'mac: %s' % (str(sl.mac)))
        print(u'sl: %s' % (sl.__dict__))
        print(u'id: %s' % (sl.id))
        print(u'mac: %s' % (sl.mac))
        print(u'ip %s:' % (sl.ip))
        print(u'hostname: %s' % (sl.hostname))
        print(u'host.vendor_name %s:' % (getattr(sl.host,u'vendor_name',u'')))
        print(u'host:\r\n--- %s\r\n--- \r\n' % (sl.host))
        print(u'comment:%s ' % (sl.comment))
        print(u'---')
        
    sl =app.new_static_lease({u'mac':u'00:04:04:04:04:04',u'ip':u'192.168.0.123',u'comment':u'test'})
    sl = sl.get_by_id(u'00:04:04:04:04:04')
    print(u'sl: %s' % (sl))
    app.delete_static_lease(u'00:04:04:04:04:04')
        
if __name__ == "__main__":

    main()

    quit(0)