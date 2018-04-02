from urllib import request, parse

"""
General:
    Request URL:http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
    Request Method:POST
    Status Code:200 OK
    Remote Address:220.181.76.84:80
    Referrer Policy:no-referrer-when-downgrade

Response Headers:
    Connection:keep-alive
    Content-Encoding:gzip
    Content-Type:application/json; charset=utf-8
    Date:Fri, 02 Mar 2018 02:18:25 GMT
    Server:nginx
    Set-Cookie:YOUDAO_MOBILE_ACCESS_TYPE=0; domain=.youdao.com; expires=Sat, 02-Mar-2019 02:18:25 GMT
    Transfer-Encoding:chunked
    Vary:Accept-Encoding

Request Headers:
    Accept:application/json, text/javascript, */*; q=0.01
    Accept-Encoding:gzip, deflate
    Accept-Language:zh-CN,zh;q=0.9
    Connection:keep-alive
    Content-Length:205
    Content-Type:application/x-www-form-urlencoded; charset=UTF-8
    Cookie:OUTFOX_SEARCH_USER_ID_NCOO=901526923.248523; _ntes_nnid=d2c9f3c0ad87edc2a18d8baf7493468a,1489816879253; P_INFO=sijipingzaojia@126.com|1507340542|0|other|00&99|shd&1506756788&other#shd&370100#10#0#0|&0||sijipingzaojia@126.com; OUTFOX_SEARCH_USER_ID=1202025429@123.58.182.244; _ga=GA1.2.1223743331.1511144818; _ym_uid=1517990399796278715; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abce35wgNPW3r7TqipGhw; __lnkrntdmcvrd=-1; ___rl__test__cookies=1519957105235
    Host:fanyi.youdao.com
    Origin:http://fanyi.youdao.com
    Referer:http://fanyi.youdao.com/?keyfrom=dict2.top
    User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36
    X-Requested-With:XMLHttpRequest

Quert String Parameyters:
    smartresult:dict
    smartresult:rule

Form Data:
    i:hello
    from:AUTO
    to:AUTO
    smartresult:dict
    client:fanyideskweb
    salt:1519957105239
    sign:8576918dd13c8c792aabc6986380a8bb
    doctype:json
    version:2.1
    keyfrom:fanyi.web
    action:FY_BY_CLICKBUTTION
    typoResult:false
"""


def doDict(keyword):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        "Connection": "keep - alive",
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Mobile Safari/537.36',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http: // fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/?keyfrom=dict2.top',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=901526923.248523; _ntes_nnid=d2c9f3c0ad87edc2a18d8baf7493468a,1489816879253; P_INFO=sijipingzaojia@126.com|1507340542|0|other|00&99|shd&1506756788&other#shd&370100#10#0#0|&0||sijipingzaojia@126.com; OUTFOX_SEARCH_USER_ID=1202025429@123.58.182.244; _ga=GA1.2.1223743331.1511144818; _ym_uid=1517990399796278715; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abce35wgNPW3r7TqipGhw; __lnkrntdmcvrd=-1; YOUDAO_MOBILE_ACCESS_TYPE=0; ___rl__test__cookies=1519960368231',
    }
    req = request.Request("http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule", headers=headers)
    data = {
        'i': keyword,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1519960368238',
        'sign': '1078dab49931bac7081851a7da7320b2',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'false',
    }
    encode_data = bytes(parse.urlencode(data), encoding='utf-8')
    response = request.urlopen(req, data=encode_data)
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    keyword = input("请输入要翻译的单词：")
    doDict(keyword)
