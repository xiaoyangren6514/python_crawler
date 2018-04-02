import http.cookiejar
from urllib import request, parse


def demo():
    # 1. 构建一个CookieJar对象实例来保存cookie
    cookie = http.cookiejar.CookieJar()
    # 2. 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
    cookie_handler = request.HTTPCookieProcessor(cookie)
    # 3. 通过 build_opener() 来构建opener
    opener = request.build_opener(cookie_handler)

    # 4. addheaders 接受一个列表，里面每个元素都是一个headers信息的元祖, opener将附带headers信息
    opener.addheaders = [("User-Agent",
                          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]
    # 5. 需要登录的账户和密码
    data = {"email": "xxx@163.com", "password": "123456opmhsa"}
    # 6. 通过urlencode()转码
    postdata = bytes(parse.urlencode(data), encoding='utf-8')
    # 7. 构建Request请求对象，包含需要发送的用户名和密码
    req = request.Request("http://www.renren.com/PLogin.do", data=postdata)
    # 8. 通过opener发送这个请求，并获取登录后的Cookie值，
    opener.open(req)
    # 9. opener包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
    response = opener.open("http://www.renren.com/410043129/profile")
    # 10. 打印响应内容
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    demo()
