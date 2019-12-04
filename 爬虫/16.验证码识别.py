import json
import base64
import requests

with open(r'C:\Users\15274\Pictures\Saved Pictures\22.png', 'rb') as fp:
    image = fp.read()
image_b64 = base64.b64encode(image)
url = 'http://codevirify.market.alicloudapi.com/icredit_ai_image/verify_code/v1'
data = {
    'IMAGE':image_b64,
    'IMAGE_TYPE':0,
}
appcode ='dd5f08fe21ff4d11a9e3b712be8be748'
headers = {
    'Authorization':'APPCODE '+appcode,
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}
response = requests.post(url=url, data=data, headers=headers).content.decode('utf-8')
code = json.loads(response)
print(code['VERIFY_CODE_ENTITY']['VERIFY_CODE'])