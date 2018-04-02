from  bs4 import BeautifulSoup
import re


def demo1():
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story p </b></p>
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
    print(type(soup.select('title')))
    print(soup.select('title')[0].get_text())

    for title in soup.select('title'):
        print(title.get_text())
    # print(soup.select('head > title'))
    # print(soup.select('p #link1'))
    # print(soup.select('#link1'))
    # print(soup.select('.sister'))
    # print(soup.select('title'))
    # print(soup.select('a'))
    # print(soup.select('p'))


if __name__ == '__main__':
    demo1()
