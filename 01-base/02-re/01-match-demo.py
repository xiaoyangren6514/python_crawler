import re


def demo2():
    # re.I表示忽略大小写
    pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
    content = 'hello world hello python'
    m = pattern.match(content)
    # 打印匹配成功的整个字符串
    print(m.group())
    # 打印整个匹配字符串的起始和结束位置
    print(m.span())
    # 打印第一个分组匹配成功字符串的起始和结束位置
    print(m.span(1))
    # 打印第一个分组匹配成功字符串的起始和结束位置
    print(m.span(2))
    # 打印第一个分组匹配成功的子串
    print(m.group(1))
    # 打印第二个分组匹配成功的子串
    print(m.group(2))
    # 打印所有的分组
    print(m.groups())


def demo():
    p1 = re.compile(r'\d+')
    content = 'hello 123 world'
    # 查找头部 没有匹配，返回None
    m1 = p1.match(content)
    print(m1)
    # 从角标6到角标9的位置进行查找，此时有值，返回Match对象
    m2 = p1.match(content, 6, 9)
    print(m2)
    # group 用于获得一个或多个分组匹配的字符串，当获取整个匹配的子串时，可以直接使用group()或group(0)
    print(m2.group())
    # start 获取分组匹配的子串在整个字符串中的起始位置
    print(m2.start())
    # end 获取分组匹配的子串在整个字符串中的结束位置
    print(m2.end())
    # span 返回(start,end)
    print(m2.span())



    # m2 = p1.match(content, 6, 12)
    # print(m2)
    # print(m2.group())
    # print(m2.span())


if __name__ == '__main__':
    demo2()
