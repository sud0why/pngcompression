import os
import requests
import re

i = 0

def get():
    for root,dirs,files in os.walk(os.getcwd()):
        for filename in files:
            if (root==os.getcwd()):
                if (str(file)[-4:]=='.png'):
                    print filename
                    download(filename)

def download(filename):
    headers = {'Connection': 'close', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0'}
    url = "http://www.atool.org/pngcompression.php"
    read = open(filename,'rb')
    files ={'pic':('test.png',read,'image/png'),'rate':(None,'10'),'action':(None,'make')}
    r = requests.post(url=url,headers=headers,files=files)
    write = open('tmp','wb')
    write.write(r.content)
    write.close()
    m = open('tmp','r').read()
    z = re.compile('<br><a[\s]href=\"[a-zA-Z]+\/[\d]+\.png\"?').findall(m)[0]
    open('tmp','r').close()
    hou = re.compile('\"').split(z)[1]
    r = requests.get("http://www.atool.org/" + hou)
    write = open('filename[:-4]'+'-1.png','wb')
    write.write(r.content)
    r.close()

if __name__ == '__main__':
    get()