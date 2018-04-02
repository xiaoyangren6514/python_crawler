import re


def demo():
    p = re.compile(r'[\s,\t;]+')
    m = p.split('a, k b;;cd\tuu')
    print(m)


if __name__ == '__main__':
    demo()
