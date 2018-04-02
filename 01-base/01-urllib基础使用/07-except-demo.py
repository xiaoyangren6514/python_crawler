from urllib import request, error
import socket


def demo3():
    try:
        request.urlopen("http://www.baidu.com", timeout=0.001)
    except error.URLError as e:
        print(type(e.reason))
        if isinstance(e.reason, socket.timeout):
            print('连接超时')


def demo2():
    try:
        resp = request.urlopen("http://www.csdn.net/abcs.html")
        print(resp.read().decode('utf-8'))
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers)
    except error.URLError as e:
        print(e.reason)
    else:
        print('success')


def demo():
    try:
        resp = request.urlopen("http://www.baiduasw.com")
        print(resp.read().decode('utf-8'))
    except error.URLError as e:
        print(e.reason)


if __name__ == '__main__':
    demo3()
