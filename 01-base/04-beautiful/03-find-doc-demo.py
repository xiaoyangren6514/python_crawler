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
    print(soup.find_all(text='Elsie'))
    print(soup.find_all(text=re.compile('^Ti')))
    print(soup.find_all(text=['Lacie', 'Tillie']))
    # print(soup.find_all(id='link3'))
    # print(soup.find_all(['a','b']))
    # b_list = soup.find_all(re.compile('^b'))
    # for tag in b_list:
    #     print(tag.name)
    # print(soup.find_all('b'))
    # print(soup.find_all('a'))


if __name__ == '__main__':
    demo1()
