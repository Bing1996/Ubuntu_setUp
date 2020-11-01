import os
import subprocess as sp
import os

os.system('clear')
print('processing')

port = ['8888' , '6802' , '6802' , '80' , '80']
server = ['home4ever.hopto.org' ,
         'bing4vpstw.hopto.org' ,
         'bing4vpsus.hopto.org' ,
         'baidu.com' ,
         'google.com']

for i in range(len(port)):
    #print(port[i] , server[i])
    status = sp.call(['tcping', '-p' , port[i] , '-c', '1', '-t', '1', server[i]], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    print (server[i] + ' status: ' , int(status))
