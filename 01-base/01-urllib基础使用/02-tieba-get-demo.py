from urllib import request, parse
import ssl

"""
通过浏览器抓取URL发现，其真实URL为：http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
kw为关键词
ie为编码格式
pn为查询列表起始位置，计算公式为：(current_page -1) * 50
"""


def spiderHtml(page, fullurl):
    print('*' * 15 + '正在爬取第' + str(page) + '页数据')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36'
    }
    context = ssl._create_unverified_context()
    req = request.Request(fullurl, headers=headers)
    response = request.urlopen(req, context=context)
    print('*' * 15 + '第' + str(page) + '页数据爬取完成')
    return response.read()


def savehtml(page, html):
    """
    保存抓取的页面数据
    :param page: 当前页
    :param html: 页面数据
    :return:
    """
    with open('num' + str(page) + '.html', mode='wb+') as f:
        print('正在保存第%d页信息' % page)
        f.write(html)
        print('第%d页信息保存成功' % page)


def mainEntrance(url, startpage, endpage):
    """
    爬虫主入口
    :param url: 基础URL
    :param startpage: 起始页
    :param endpage: 结束页
    :return:
    """
    for page in range(startpage, endpage + 1):
        pn = (page - 1) * 50
        fullurl = url + '&' + str(pn)
        html = spiderHtml(page, fullurl)
        savehtml(page, html)


if __name__ == '__main__':
    keyword = input("请输入贴吧名:")
    startpage = int(input("请输入起始页:"))
    endpage = int(input("请输入结束页:"))
    data = {
        'kw': keyword
    }
    encodeData = parse.urlencode(data)
    url = 'http://tieba.baidu.com/f?' + encodeData
    mainEntrance(url, startpage, endpage)
