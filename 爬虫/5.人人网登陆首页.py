import random

import requests

# enter_url = "http://www.renren.com/PLogin.do"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
#             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}
#
#
#
# res = requests.session()
# data = {'email':'17803373056', "password":"13483648816"}
# res.post(url=enter_url, headers=headers, data=data, )
#
# url = "http://www.renren.com/972926006/profile"
# response = res.get(url=url, headers=headers, ).content.decode('utf-8')
#
# with open('renrenprofile.html', 'w', encoding='utf-8') as fp:
#     fp.write(response)

url = "http://www.renren.com/972926006/profile"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
'Cookie': 'wp_fold=0; anonymid=k3du4n9obo76mj; depovince=BJ; jebecookies=0ce07049-e0fe-4725-b59b-4995bba19814|||||; _r01_=1; JSESSIONID=abcjJBeMyXMvo8eblEG6w; ick_login=f1773c81-8fac-4420-91f6-879c587c56ed; _de=A12531EE8F0B2CAA56F3773D82F8A017; p=6f208e2625507b6ac0c6cb90c36d16aa6; first_login_flag=1; ln_uact=17803373056; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=8d9e45f00b9014f1f2c6231f9a39f8876; societyguester=8d9e45f00b9014f1f2c6231f9a39f8876; id=972926006; xnsid=5f86f58f; ver=7.0; loginfrom=null'
           }
response = requests.get(url=url, headers=headers).content.decode('utf-8')
with open("renren2.html", 'w', encoding='utf-8') as fp:
    fp.write(response)
