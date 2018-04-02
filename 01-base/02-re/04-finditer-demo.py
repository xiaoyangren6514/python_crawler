import re


def demo():
    p = re.compile(r'\d+')
    m = p.finditer('123hello412as999')
    for item in m:
        print(item.group(), item.span())


if __name__ == '__main__':
    demo()
