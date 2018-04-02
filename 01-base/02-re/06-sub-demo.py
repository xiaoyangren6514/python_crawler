import re


def demo():
    p = re.compile(r'(\w+) (\w+)')
    str = 'hello 123,hello 456'
    # sub 使用'hello python' 替换匹配到的 'hello' '123'
    print(p.sub('hello python', str))
    # 引用分组
    print(p.sub(r'\2 \1', str))
    print('*' * 20)
    print(p.sub(fun_demo, str))
    # 最多替换一次
    print(p.sub(fun_demo, str, 1))


def fun_demo(m):
    return 'hi ' + m.group(2)


if __name__ == '__main__':
    demo()
