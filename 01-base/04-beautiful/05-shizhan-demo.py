from bs4 import BeautifulSoup
from urllib import request
import ssl
import json

# 存储段子列表
duanzilist = []


def demo():
    # 通过浏览器查看不同页面url变化
    url = 'https://www.qiushibaike.com/8hr/page/2/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    # 忽略https校验
    context = ssl._create_unverified_context()
    req = request.Request(url, headers=headers)
    response = request.urlopen(req, context=context)
    content = response.read().decode('utf-8')
    # 转换bs对象
    soup = BeautifulSoup(content, 'lxml')
    # 通过class值获取段子列表
    content_list = soup.find_all(
        class_=['article block untagged mb15 typs_recent', 'article block untagged mb15 typs_hot',
                'article block untagged mb15 typs_old'])
    for content in content_list:
        # 将每条段子列表转换成bs对象
        div_soup = BeautifulSoup(str(content), 'lxml')
        # print(div_soup.prettify())
        # 获取昵称
        nickname = div_soup.find_all('h2')[0].get_text().strip()
        # 获取年龄
        if nickname == '匿名用户':
            age = 0
        else:
            age = div_soup.find_all(class_=['articleGender manIcon', 'articleGender womenIcon'])[0].get_text().strip()
        # 获取头像 {'alt': '『阿布』', 'src': '//pic.qiushibaike.com/system/avtnew/1417/14175454/thumb/20180327133623.JPEG?imageView2/1/w/90/h/90'}
        imageurl = div_soup.img.attrs['src']
        # 获取文本内容
        text = div_soup.select('.content')[0].get_text().strip()
        duanzi = {
            'nickname': nickname,
            'age': age,
            'imageurl': imageurl,
            'text': text
        }
        duanzilist.append(duanzi)
        print(duanzi)
    # 写入文件
    dumps = json.dumps(duanzilist, ensure_ascii=False)
    with open('duanzi.json', 'wb') as f:
        f.write(dumps.encode('utf-8'))


if __name__ == '__main__':
    demo()
