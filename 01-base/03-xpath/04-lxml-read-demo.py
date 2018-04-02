from lxml import etree


def getContent():
    html = etree.parse('./hello.html')
    result = etree.tostring(html, pretty_print=True)
    return html


def getClassBoldTag():
    html = getContent()
    result = html.xpath('//*[@class="bold"]')
    print(result[0].tag)


def getLast2Content():
    html = getContent()
    result = html.xpath('//li[last()-1]/a')
    print(result[0].text)


def getLastLiAHref():
    html = getContent()
    result = html.xpath('//li[last()]/a/@href')
    print(result)


def getLiAClass():
    html = getContent()
    result = html.xpath('//li/a//@class')
    print(result)


def getLiSpan():
    html = getContent()
    result = html.xpath('//li//span')
    print(result)


def getLiHref():
    html = getContent()
    result = html.xpath('//li/a[@href="link1.html"]')
    print(result)


def getLiClass():
    html = getContent()
    result = html.xpath('//li/@class')
    print(result)


def getAllLi():
    html = getContent()
    # 打印etree.parse返回类型
    print(html)
    result = html.xpath('//li')
    # 打印查找到的集合
    print(result)
    # 打印查找集合长度
    print(len(result))
    # 打印集合类型
    print(type(result))
    # 打印集合中第一个元素类型
    print(type(result[0]))


if __name__ == '__main__':
    getClassBoldTag()
