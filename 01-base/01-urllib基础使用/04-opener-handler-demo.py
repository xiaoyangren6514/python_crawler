from urllib import request
import random

"""
HTTPPasswordMgrWithDefaultRealm
    创建一个密码管理对象，用来保存HTTP请求相关的用户名和密码。
主要两个场景：
1、验证代理授权的用户名和密码（proxyBasicAuthHandler）
2、验证web客户端的用户名和密码(HttpBasicAuthHandler)

"""


def pwd_demo2():
    # 私密代理授权的账户 密码
    user = 'wangcai'
    pwd = '12345qwertyui'
    # 私密代理IP
    web_server = '119.129.99.29:1231'
    # 构建一个密码管理对象，保存用户名和密码
    pwdmgr = request.HTTPPasswordMgrWithDefaultRealm()
    # 添加账户信息
    pwdmgr.add_password(None, web_server, user=user, passwd=pwd)
    # 构建一个代理基础用户名/密码验证的HttpBasicAuthHandler对象，参数是创建的密码管理对象
    proxy_handler = request.HTTPBasicAuthHandler(pwdmgr)
    # 通过build_opener方法使用Handler创建自定义opener
    opener = request.build_opener(proxy_handler)
    # 构造request请求
    req = request.Request("http://www.baidu.com")
    # 发送请求并打印响应（requesr.install_opener()执行后，全局生效）
    response = opener.open(req)
    print(response.read().decode('utf-8'))


def pwd_demo():
    # 私密代理授权的账户 密码
    user = 'demo'
    pwd = '1234'
    # 私密代理IP
    proxy_server = '119.129.99.29:1231'
    # 构建一个密码管理对象，保存用户名和密码
    pwdmgr = request.HTTPPasswordMgrWithDefaultRealm()
    # 添加账户信息
    pwdmgr.add_password(None, proxy_server, user=user, passwd=pwd)
    # 构建一个代理基础用户名/密码验证的ProxyBasicAuthHandler对象，参数是创建的密码管理对象
    proxy_handler = request.ProxyBasicAuthHandler(pwdmgr)
    # 通过build_opener方法使用Handler创建自定义opener
    opener = request.build_opener(proxy_handler)
    # 构造request请求
    req = request.Request("http://www.baidu.com")
    # 发送请求并打印响应
    response = opener.open(req)
    print(response.read().decode('utf-8'))


def handler_demo2():
    """
    代理足够多，可以随机选择一个去访问
    :return:
    """
    proxy_list = [
        {"http": "101.200.24.123:80"},
        {"http": "101.200.24.123:80"},
        {"http": "101.200.24.123:80"},
        {"http": "101.200.24.123:80"},
    ]
    proxy = random.choice(proxy_list)
    handler = request.ProxyHandler(proxy)
    opener = request.build_opener(handler)
    req = request.Request("http://www.baidu.com")
    response = opener.open(req)
    print(response.read().decode('utf-8'))


def handler_demo():
    # 构建两个Handler，一个有代理IP，一个无
    httpproxy_handler = request.ProxyHandler({"http": "139.224.135.94:80"})
    nullproxy_handler = request.ProxyHandler()
    # 通过build_opener方法使用Handler代理对象，创建自定义opener
    opener = request.build_opener(httpproxy_handler)
    # 构建request请求
    req = request.Request("http://www.baidu.com")
    # 使用代理，只有opener.open才会生效，urlopen无效
    response = opener.open(req)
    print(response.read().decode('utf-8'))
    # 如果使用request.install_opener(opener)，那么不管使用opener.open()还是urlopen()都将使用代理


def opener_demo():
    # 构建一个HTTPHandler处理器对象，支持HTTP请求
    http_handler = request.HTTPHandler(debuglevel=1)
    # 调用urllib.request的build_opener方法，创建支持http请求的opener对象
    opener = request.build_opener(http_handler)
    # 构建request请求
    req = request.Request("http://www.baidu.com")
    # 使用自定义opener对象的open方法，发送request请求
    response = opener.open(req)
    # 获取server响应
    # print(response.read().decode('utf-8'))


if __name__ == '__main__':
    handler_demo()
