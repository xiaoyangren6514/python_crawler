import requests
import threading
from queue import Queue
import time
from lxml import etree
import json


class ThreadCrawl(threading.Thread):
    """
    抓取线程
    """

    def __init__(self, name, pageQueue, dataQueue):
        super(ThreadCrawl, self).__init__()
        # 线程名
        self.name = name
        # 抓取页码队列
        self.pageQueue = pageQueue
        # 抓取结果数据队列
        self.dataQueue = dataQueue
        # 设置请求头
        self.headers = {
            # 'Host': 'www.qiushibaike.com',
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # 'Accept-Language:': 'zh-CN,zh;q=0.9',
            # 'Connection': 'keep-alive',
            # 'Cookie': '_xsrf=2|56a30360|dae0d6d1fa904f207ba782b251873f73|1522127045',
            # 'Upgrade-Insecure-Requests':'1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36',
        }

    def run(self):
        print(self.name + ' start ')
        while not CRAWL_EXIT:
            try:
                page = self.pageQueue.get(False)
                url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + "/"
                content = requests.get(url, headers=self.headers).text
                print('*' * 100)
                print(url)
                with open('qiubai_' + str(page) + '.html', 'wb') as f:
                    f.write(content.encode('utf-8'))
                print(content)
                print('*' * 100)
                time.sleep(1)
                self.dataQueue.put(content)
            except:
                pass
        print(self.name + ' end ')


class ThreadParse(threading.Thread):
    def __init__(self, name, dataQueue, file, lock):
        super(ThreadParse, self).__init__()
        # 线程名
        self.name = name
        # 解析数据队列
        self.dataQueue = dataQueue
        # 文件(写数据)
        self.file = file
        # 文件锁
        self.lock = lock

    def run(self):
        print(self.name + ' start ')
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                self.doParse(html)
            except:
                pass
        print(self.name + ' end ')

    def doParse(self, html):
        html = etree.HTML(html)
        node_list = html.xpath('//div[contains(@class, "item")]')

        for node in node_list:
            # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
            username = node.xpath('./div/a/@title')[0]
            # 图片连接
            image = node.xpath('.//div[@class="thumb"]//@src')  # [0]
            # 取出标签下的内容,段子内容
            content = node.xpath('.//div[@class="content"]/span')[0].text
            # 取出标签里包含的内容，点赞
            zan = node.xpath('.//i')[0].text
            # 评论
            comments = node.xpath('.//i')[1].text

            items = {
                "username": username,
                "image": image,
                "content": content,
                "zan": zan,
                "comments": comments
            }
            print(items)
            # with 后面有两个必须执行的操作：__enter__ 和 _exit__
            # 不管里面的操作结果如何，都会执行打开、关闭
            # 打开锁、处理内容、释放锁
            with self.lock:
                # 写入存储的解析后的数据
                self.file.write(json.dumps(items, ensure_ascii=False).encode("utf-8") + "\n")


CRAWL_EXIT = False
PARSE_EXIT = False


def main():
    output = open('qiushibaike.json', 'a')

    # 初始化目标页码
    pageQueue = Queue(50)
    for page in range(1, 5):
        pageQueue.put(page)

    # 采集结果(html)
    dataQueue = Queue()

    # 初始化采集线程
    crawlThreads = []
    crawlNameList = ['crawl-1', 'crawl-2', 'crawl-3']
    for name in crawlNameList:
        thread = ThreadCrawl(name, pageQueue, dataQueue)
        crawlThreads.append(thread)
        thread.start()

    # 创建锁
    lock = threading.Lock()

    # 初始化解析线程
    parseTheads = []
    parseNameList = ['parse-1', 'parse-2', 'parse-3']
    for name in parseNameList:
        thread = ThreadParse(name, dataQueue, output, lock)
        thread.start()
        parseTheads.append(thread)

    # 等待pageQueue队列为空(等待之前的操作执行完毕)
    while not pageQueue.empty():
        pass

    # 如果pageQueue为空，抓取线程为空
    global CRAWL_EXIT
    CRAWL_EXIT = True

    print('*' * 10 + 'pageQueue empty' + '*' * 10)

    for thread in crawlThreads:
        thread.join()
        print('1')

    # 等待dataQueue队列为空(等待之前的操作执行完毕)
    while not dataQueue.empty():
        pass

    # 如果dataQueue为空，通知线程退出
    global PARSE_EXIT
    PARSE_EXIT = True

    for thread in parseTheads:
        thread.join()
        print('2')

    # 关闭文件
    with lock:
        output.close()

    print('抓取结束，感谢您的使用')


if __name__ == '__main__':
    main()
