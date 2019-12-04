import requests
from lxml import etree

url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=20746041'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
response = requests.get(url=url,  headers=headers, verify=False).content

tree = etree.HTML(response)
data = tree.xpath('//d/text()')
for i in data:
    print(i)