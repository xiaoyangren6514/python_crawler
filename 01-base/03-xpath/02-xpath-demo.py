from urllib import request
import ssl
from lxml import etree


def load_list_page():
    url = 'https://b.faloo.com/y/0/0/0/0/8/2/1.html'
    headers = {
        # 'Cookie': 'JSESSIONID=abcO27KBuA3k7brmwXuiw',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36',
        # 'Host': 'hao123.zongheng.com',
        # 'Referer': 'http://hao123.zongheng.com/store/c1/w0/s0/p1/all.html',
        # 'Upgrade-Insecure-Requests': '1',
        # 'Connection': 'keep-alive',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cache-Control': 'max-age=0',
        # 'Accept-Encoding':'gzip, deflate, br'

    }
    context = ssl._create_unverified_context()
    req = request.Request(url, headers=headers)
    response = request.urlopen(req, context=context)
    html = response.read().decode('gbk')
    content = etree.HTML(html)
    name_list = content.xpath('/html/body/div[9]/div[1]/div[1]/div/div[2]/div[1]/h1/a/@title')
    link_list = content.xpath('/html/body/div[9]/div[1]/div[1]/div/div[2]/div[1]/h1/a/@href')
    print(name_list)
    for link in link_list:
        print('*'*30)
        url = 'https:'+link
        req = request.Request(url, headers=headers)
        response = request.urlopen(req, context=context)
        html = response.read().decode('gbk')
        content = etree.HTML(html)
        chap_title = content.xpath('/html/body/div[8]/div[1]/div/div[3]/div[2]/table[4]/tbody/tr/td/a/text()')
        for title in chap_title:
            print(title)

if __name__ == '__main__':
    load_list_page()
