from lxml import etree


def demo():
    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a>
         </ul>
     </div>
    '''

    # 利用etree.HTML，将字符串解析为HTML文档
    html = etree.HTML(text)
    # 按字符串序列化HTML文档
    result = etree.tostring(html)
    print(result.decode('utf-8'))


if __name__ == '__main__':
    demo()
