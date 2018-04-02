import re


def demo2():
    p = re.compile(r'\d+')
    content = 'hello123world'
    m = p.search(content)
    if m:
        print('match str:' + m.group())
        print('position:', m.span())


def demo():
    p = re.compile(r'\d+')
    content = 'hello123world'
    m = p.search(content)  # 此时match匹配返回None
    # 打印匹配到的数据
    print(m.group())
    # 打印匹配到的字符串在整串中的起始位置
    print(m.start())
    # 打印匹配到的字符串在整串中的结束位置
    print(m.end())
    # 打印匹配到的字符串在整串中的起始和结束位置
    print(m.span())


if __name__ == '__main__':
    demo2()
