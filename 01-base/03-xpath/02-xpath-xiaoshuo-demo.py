from urllib import request
import ssl
import zlib
import gzip
from lxml import etree

from io import StringIO, BytesIO


class Spider():
    def __init__(self, baseurl, url):
        # 通过Chrome开发者工具，查看浏览器中发送请求是header，同步下来
        self.headers = {
            'Cookie': '_csrfToken=h2SMbKQwIwllQZriok57byvGBpPi8oOBUmjvItL2; newstatisticUUID=1520855551_762608354',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36',
            'Host': 'www.hongxiu.com',
            'Referer': 'https://www.hongxiu.com/rank/hxyuepiao',
            'Upgrade-Insecure-Requests': '1',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'text/html;charset=utf-8',
        }
        # 忽略https校验
        self.context = ssl._create_unverified_context()
        self.baseurl = baseurl
        self.url = url

    def gzipData(self, data):
        """
        使用gzip方式解压缩数据
        :param data:
        :return:
        """
        buf = BytesIO(data)
        f = gzip.GzipFile(fileobj=buf)
        return f.read()

    def deflate_data(self, data):
        """
        使用deflate方式解压缩数据
        :param data:
        :return:
        """
        try:
            return zlib.decompress(data, -zlib.MAX_WBITS)
        except zlib.error:
            return zlib.decompress(data)

    def ungzip(self, data):
        """
            使用gzip方式解压缩数据
        """
        data = gzip.decompress(data)
        return data

    def loadPageContent(self, url):
        """
        加载数据
        :param url:
        :return:
        """
        req = request.Request(url, headers=self.headers)
        response = request.urlopen(req, context=self.context)
        content = response.read()
        encoding = response.info().get('Content-Encoding')
        # 判断返回的encoding格式
        if encoding == 'gzip':
            content = self.gzipData(content)
        elif encoding == 'deflate':
            content = self.deflate_data(content)
        content = content.decode('utf-8')
        return content

    def load_list_page(self):
        # 加载列表数据
        content = self.loadPageContent(self.url)
        # with open('a.html', 'w+', encoding='utf-8') as f:
        #     f.write(content)
        # print(content)
        content = etree.HTML(content)
        articleTitleList = content.xpath('//*[@id="rank-view-list"]/div[1]/ul/li/div[2]/h4/a/text()')
        print(articleTitleList)
        articleLinkList = content.xpath('//*[@id="rank-view-list"]/div[1]/ul/li/div[2]/h4/a/@href')
        print(articleLinkList)
        # 开始加载每个小说对应的详情数据
        for i, value in enumerate(articleLinkList):
            print('开始获取：' + articleTitleList[i] + ' ulr ---> ' + value)
            # 拼接详情页url
            newurl = self.baseurl + value
            html = self.loadPageContent(newurl)
            content = etree.HTML(html)
            chapterTitleList = content.xpath('//*[@id="j-catalogWrap"]/div[2]/div[1]/ul/li/a/text()')
            print(chapterTitleList)
            print('获取结束：' + articleTitleList[i])
            # 此处break，只获取第一个
            break

    def startWork(self):
        self.load_list_page()


if __name__ == '__main__':
    baseurl = 'https://www.hongxiu.com'
    url = 'https://www.hongxiu.com/rank/hxyuepiao?pageNum=2'
    spider = Spider(baseurl, url)
    spider.startWork()
