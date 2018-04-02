import requests
from requests.packages import urllib3


def main():
    demo_ssl()


def demo_proxy():
    proxies = {
        "http": "http://user:pwd@10.10.1.10:3128",
    }
    proxies = {
        "http": "http://10.10.1.10:3128",
        "https": "http://10.10.1.10:1080",
    }
    url = 'http://www.baidu.com'
    requests.get(url, proxies=proxies)


def demo_ssl():
    urllib3.disable_warnings()
    url = 'https://www.12306.cn'
    resp = requests.get(url, verify=False)
    print(resp.status_code)


def demo_session():
    s = requests.session()
    s.auth = ('user', 'pass')
    s.headers.update({'x-test': 'true'})
    s.get('url', headers={'xtest2': 'aaa'})
    # s.get('http://httpbin.org/cookies/set/sessioncookie/abcsd')
    # r = s.get("http://httpbin.org/cookies")
    # print(r.text)


def demo_req_resp():
    url = 'http://www.baidu.com'
    resp = requests.get(url)
    print(resp.headers)
    print('*' * 50)
    print(resp.request.headers)


if __name__ == '__main__':
    main()
