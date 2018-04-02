from  bs4 import BeautifulSoup


def demo1():
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """
    # 创建bs对象
    soup = BeautifulSoup(html_doc, "lxml")
    print(soup.a)
    print(soup.a.name)
    print(soup.a.attrs)
    content = soup.a.string
    print(content)
    print(type(content))
    # demo_beautifulsoup(soup)
    # demo_navigablestring(soup)
    # demo_name_attrs(soup)
    # demo_tag(soup)


def demo_beautifulsoup(soup):
    print(soup.name)
    print(soup.attrs)
    print(type(soup))


def demo_navigablestring(soup):
    # 获取标签内文字
    content = soup.title.string
    print(content)
    print(type(content))


def demo_name_attrs(soup):
    # [document] #soup 对象本身比较特殊，它的 name 即为 [document]
    print(soup.name)
    # 对于其他内部标签，输出的值便为标签本身的名称
    print(soup.title.name)
    print(soup.p.name)
    print('*' * 20)
    # 把 p 标签的所有属性打印输出了出来，得到的类型是一个字典
    print(soup.p.attrs)
    # 还可以利用get方法，传入属性的名称，二者是等价的
    print(soup.p['class'])
    print(soup.p.get('class'))
    # 对属性进行修改
    soup.p['class'] = 'hello world'
    print(soup.p.attrs)
    # 删除属性
    del soup.p['class']
    print(soup.p)
    print(soup.p.attrs)


def demo_tag(soup):
    # 按照标准缩进 结构化输出html内容
    # print(soup.prettify())
    print(soup.title)
    print(soup.p)
    print(soup.a)
    print(soup.head)
    print(type(soup.body))


if __name__ == '__main__':
    demo1()
