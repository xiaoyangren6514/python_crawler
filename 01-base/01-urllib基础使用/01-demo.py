from urllib import request, parse, error
import socket


def demo4():
    try:
        resp = request.urlopen("http://www.baidu.com", timeout=0.001)
        print(resp.read().decode('utf-8'))
    except error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('timeout , stop')


def demo3():
    """
    urlopen方法中增加data参数代表是一个post请求
    设置headers，比如UA
    :return:
    """
    req = request.Request('http://www.baidu.com')
    req.add_header('User-Agent', 'Mozilla/5.0')
    data = {
        'name': 'wangcai'
    }
    resp = request.urlopen(req, data=bytes(parse.urlencode(data), encoding='utf-8'))
    print(resp.read().decode('utf-8'))


def demo2():
    """
    构建一个request对象，URL作为构造参数传入
    :return:
    """
    req = request.Request('http://www.baidu.com')
    resp = request.urlopen(req)
    print('resp:', resp.read().decode('utf-8'))


def demo1():
    """
    直接使用urlopen打开网页，返回结果可以作为一个文件对象进行操作
    :return:
    """
    with request.urlopen('http://www.baidu.com') as f:
        # 读取返回的数据
        data = f.read()
        # 请求code码 200 404 500 403
        print('code:', f.getcode())
        # 返回实际数据的URL
        print('url:', f.geturl())
        # 服务器返回的http报头信息
        print('info:', f.info())
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))


if __name__ == '__main__':
    demo4()
