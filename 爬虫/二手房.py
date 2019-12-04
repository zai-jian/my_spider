import json
import re

import requests

url = "https://esf.fang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
'cookie': 'global_cookie=qt022swgud2d26p9kyy68wpel08k3ecwi9a; Integrateactivity=notincludemc; __utmc=147393320; csrfToken=LUsz-ck0GyHj2v6vmoLI9lxR; integratecover=1; logGuid=b17ea3aa-f79e-487e-ba7b-832b09aa2912; city=www; lastscanpage=0; resourceDetail=1; Captcha=556B626275384E6D434E343361397A4B4F2F4347676A775054705532524F43316E444D375A7478417137645667782F4B776B6B4C562F344B4B755432512B36636F75356F4C71497545686F3D; g_sourcepage=esf_fy%5Elb_pc; __utma=147393320.1332610625.1574681830.1574688229.1574690435.3; __utmz=147393320.1574690435.3.3.utmcsr=zu.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; unique_cookie=U_qt022swgud2d26p9kyy68wpel08k3ecwi9a*22; __utmb=147393320.33.10.1574690435'
}
content = requests.get(url=url, headers=headers).content.decode('gbk')
dd_re = re.compile(r'<dl class="clearfix" dataflag="bg" data-bg=[\d\D]*?</dl>')
data = dd_re.findall(content)
home_list = []
for home in data:
    home_dict = {}
    # print(home)
    # title_re = re.compile('<span class="tit_shop">(.*?)</span>')
    # title = title_re.findall(home)
    # print(title)
    # img_re = re.compile('src2="(.*?)" onerror="')
    # img = img_re.findall(home)
    # print(img)
    # info_re = re.compile(r'<p class="tel_shop">\r\n(.*?)<i>\|</i>(.*?)<i>\|</i>(.*?)<i>\|</i>(.*?)<i>\|</i>(.*?)<i>\|</i><span')
    # info = info_re.findall(home)
    # if info:
    #     print(info)
    # else:
    #     print("未知")
    # place_re = re.compile(r'<span>(.*?)</span>')
    # place = place_re.findall(home)
    # print(place)
    # price_re = re.compile(r'<span class="red"><b>(.*?)</b>万</span>')
    # price = price_re.findall(home)
    # print(price)
    # broker_re = re.compile(r"target='_blank' >(.*?)</a>")
    # broker = broker_re.findall(home)
    # print(broker)









