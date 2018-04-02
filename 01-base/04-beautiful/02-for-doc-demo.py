from  bs4 import BeautifulSoup


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
    print(soup.head.string)
    print(soup.title.string)


def demo_descendants(soup):
    for child in soup.descendants:
        print(child)


def demo_children(soup):
    print(soup.head.children)
    for child in soup.body.children:
        print(child)


def demo_contents(soup):
    print(soup.head.contents)
    print(soup.body.contents)


if __name__ == '__main__':
    demo1()
