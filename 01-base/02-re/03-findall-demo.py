import re


def demo2():
    p = re.compile(r'\d+.\d*')
    m = p.findall("3.141,'asv',4.1,12,'aaa9.9vvv'")
    print(m)


def demo():
    p = re.compile(r'\d+')
    m = p.findall('123hello412as999')
    print(m)


if __name__ == '__main__':
    demo2()
