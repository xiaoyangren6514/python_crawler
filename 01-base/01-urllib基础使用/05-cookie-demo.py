from urllib import request
import http.cookiejar
import ssl


def demo4():
    """
    从文件中获取Cookie，并作为请求的一部分
    :return:
    """
    # 创建MozillaCookieJar对象
    cookie_jar = http.cookiejar.MozillaCookieJar()
    # 文件名
    cookie_filename = 'cookie_file.txt'
    # 读取cookie内容
    cookie_jar.load(cookie_filename)
    # 使用httpCookiePorcessor创建Cookie处理器对象，参数为cookieJar
    http_cookie_processor = request.HTTPCookieProcessor(cookiejar=cookie_jar)
    # 构建opener
    opener = request.build_opener(http_cookie_processor)
    # 构建request
    req = request.Request("http://www.baidu.com")
    # 发送请求
    response = opener.open(req)
    print('done')


def demo3():
    """
    获取cookie，并保存到cookie文件中
    :return:
    """
    # 文件名
    cookie_filename = 'cookie_file.txt'
    # 构建cookieJar对象来保存cookie
    cookie_jar = http.cookiejar.MozillaCookieJar(filename=cookie_filename)
    # 使用httpCookiePorcessor创建Cookie处理器对象，参数为cookieJar
    http_cookie_processor = request.HTTPCookieProcessor(cookiejar=cookie_jar)
    # 构建opener
    opener = request.build_opener(http_cookie_processor)
    # 构建request
    req = request.Request("http://www.baidu.com")
    # 发送请求
    response = opener.open(req)
    # 保存cookie信息
    cookie_jar.save()
    print('done')


def demo2():
    """
    获取cookie，并保存在cookieJar对象中
    :return:
    """
    # 构建cookieJar对象来保存cookie
    cookie_jar = http.cookiejar.CookieJar()
    # 使用httpCookiePorcessor创建Cookie处理器对象，参数为cookieJar
    http_cookie_processor = request.HTTPCookieProcessor(cookiejar=cookie_jar)
    # 构建opener
    opener = request.build_opener(http_cookie_processor)
    # 构建request
    req = request.Request("http://www.baidu.com")
    # 发送请求
    response = opener.open(req)
    # 打印cookie信息
    for item in cookie_jar:
        print(item.name + '=' + item.value)
    print('done')


def demo():
    # 通过Chrome开发者工具获取到的headers信息
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': ':zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # 如果没有这个数据，会获取不到内容
        'Cookie': 'SINAGLOBAL=4451465401860.67.1489663918038; UOR=,,www.cidu.com.cn; ULV=1512638074353:39:2:1:654449358996.8848.1512638074260:1512122654080; YF-Page-G0=3d55e26bde550ac7b0d32a2ad7d6fa53; __lnkrntdmcvrd=-1; login_sid_t=764ee242ec6c2c671008097fe81d9776; cross_origin_proto=SSL; YF-Ugrow-G0=ad83bc19c1269e709f753b172bddb094; YF-V5-G0=020421dd535a1c903e89d913fb8a2988; WBStorage=c5ff51335af29d81|undefined; WBtopGlobal_register_version=d7a77880fa9c5f84; SCF=ApB-0Hdxe1pH2EVUwj6T7lnFDhHVmpTrGutTGUCBqAxNpYokCZKUXDXjFb7jnhhuX52vPbRLRqP7Q1qC5LF6HDE.; SUB=_2A253mhxmDeRhGeVG71AR-SjEzz-IHXVU7gqurDV8PUNbmtANLUOjkW9NT7lHG3qdhhmQlBxLcF_jvJiQRxBGY_6P; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh16762MDLHTnQwjrekN9-b5JpX5KzhUgL.FoeRShz71KqRShe2dJLoIEXLxK-LBo5L12qLxKqLBoBL12zLxKBLB.2LB.2LxKqL1-eL1hWQqPW7wKz7eKnt; SUHB=0FQbL0-bhmNpOg; ALF=1551867826; SSOLoginState=1520331826; wvr=6; wb_timefeed_3842096843=1',
        'Host': 'weibo.com',
        'Referer': 'https://weibo.com/u/3842096843/home?leftnav=1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'ozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    }
    url = 'https://weibo.com/fav?leftnav=1&pids=plc_main&ajaxpagelet=1&ajaxpagelet_v6=1&__ref=%2Fu%2F3842096843%2Fhome%3Fleftnav%3D1&_t=FM_152033182791241'
    # 构建request对象
    req = request.Request(url, headers=headers)
    # 不验证https
    context = ssl._create_unverified_context()
    # 发送请求
    response = request.urlopen(req, context=context)
    # 打印响应内容
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    demo3()
