import re
from urllib import request
import ssl


def demo():
    urls = [
        'https://www.qiushibaike.com/8hr/page/2/',
        'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1520488008',
        'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1520482008',

    ]
    url = 'https://www.qiushibaike.com/8hr/page/2/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36',
        'Cookie': 'csrftoken=64da030e3ba4a02f9f245124fc219dbc; tt_webid=6530496514594244099; uuid="w:74e28436299846bf99daeaddde663b94"; __lnkrntdmcvrd=-1',
        # 'Host': 'neihanshequ.com',
        'Referer': 'http://neihanshequ.com',
        'X-CSRFToken': '64da030e3ba4a02f9f245124fc219dbc',
        'X-Requested-With': 'XMLHttpReques',

    }
    context = ssl._create_unverified_context()
    req = request.Request(url, headers=headers)
    response = request.urlopen(req, context=context)
    content = response.read().decode('utf-8')
    with open('qb.html', 'w+', encoding='utf-8') as f:
        f.write(content)
    print(content)


if __name__ == '__main__':
    demo()
