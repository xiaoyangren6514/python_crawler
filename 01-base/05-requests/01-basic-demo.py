import requests
from io import BytesIO
from PIL import Image
import json


def main():
    demo_response()


def demo_cookies():
    cookies = dict(cookies_are='working')
    resp = requests.get('http://www.baidu.com', cookies=cookies)
    print(resp.text)
    for item in resp.cookies.items():
        print(item)
    print(resp.cookies)
    print(resp.cookies.get('BDORZ'))


def demo_resp_headers():
    resp = requests.get('http://www.baidu.com')
    print(resp.headers)
    print(resp.headers['Server'])
    print(resp.headers.get('Content-Type'))


def demo_status_code():
    resp = requests.get('http://www.snsd.com/404/aaa.html')
    print(resp.status_code)
    print(resp.status_code == requests.codes.ok)
    resp.raise_for_status()


def demo_upload_file():
    url = 'http://www.baidu.com'
    files = {'file': open('test.ppt', 'rb')}
    response = requests.post(url, files=files)


def demo_fuza_post():
    url = 'http://www.baidu.com'
    data = {'name': '旺财', 'age': 12}
    print(json.dumps(data))
    # resp = requests.post(url, data=json.dumps(data))
    resp = requests.post(url, json=data)


def demo_add_headers():
    url = 'http://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)


def demo_resp_origin():
    url = 'http://www.baidu.com'
    resp = requests.get(url, stream=True)
    print(resp.raw)
    print(resp.raw.read(12))


def demo_json():
    response = requests.get('https://api.github.com/events')
    print(response.json())


def demo_image():
    # 图片URL
    url = 'http://d.hiphotos.baidu.com/image/pic/item/8435e5dde71190efbdcd14ddc21b9d16fdfa60fa.jpg'
    resp = requests.get(url)
    image = Image.open(BytesIO(resp.content))
    print(image)


def demo_response():
    url = 'https://www.baidu.com'
    resp = requests.get(url)
    print(resp.status_code)
    print(resp.encoding)
    print(resp.reason)
    # resp.encoding = 'gbk'
    # print(resp.encoding)
    print(resp.text)


def demo_post():
    url = 'http://www.baidu.com'
    data = {'name': '旺财', 'age': 12}
    resp = requests.post(url, data=data)


def demo_get():
    params1 = {'name': '旺财', 'age': 12}
    resp = requests.get('http://www.baidu.com', params=params1)
    print(resp.url)
    print('*' * 50)
    params2 = {'name': 'zhangsan', 'age': 34, 'location': ['bj', 'sh']}
    resp = requests.get('http://www.baidu.com', params=params2)
    print(resp.url)


if __name__ == '__main__':
    main()
