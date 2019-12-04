import json
import random

import requests


city_url = "https://www.amap.com/service/cityList?version=20191127"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}
proxies = [{"http": "115.221.243.207:9999", },
           {"http": "123.163.122.139:9999", },
           {"http": "58.22.177.191:9999", },
           {"http": "27.152.2.40:9999", },
           ]
proxy = random.choice(proxies)
print(proxy)
# 请求接口返回城市的name 和 编码
city_response = requests.request(url=city_url, method="get", headers=headers, proxies=proxy).content.decode("utf-8")
city_response = json.loads(city_response)

for i in city_response["data"]["cityByLetter"].values():
    for j in i:
        print(j["name"])
        url = "https://www.amap.com/service/weather?adcode={}".format(j['adcode'])
        response = requests.request(url=url, method="get", headers=headers, proxies=proxy).content.decode("utf-8")
        response = json.loads(response)
        try:
            city_data = response["data"]["data"]
            for i in city_data:
                print("{}  周{}".format(i["forecast_date"], i["weekday"]+1))
                print("{}  最高温度{}  最低温度{} {} {}级".format(i["forecast_data"][0]["weather_name"],
                                                          i["forecast_data"][0]["max_temp"],
                                                          i["forecast_data"][0]["min_temp"],
                                                          i["forecast_data"][0]["wind_direction_desc"],
                                                          i["forecast_data"][0]["wind_power_desc"]))
                #  拼接字符串以便写入
                city_weather = "{} \n {}  周{}\n{}  最高温度{}  最低温度{} {} {}级\n".format(j["name"],
                                                                                i["forecast_date"],
                                                                                i["weekday"]+1,
                                                                                i["forecast_data"][0]["weather_name"],
                                                                                i["forecast_data"][0]["max_temp"],
                                                                                i["forecast_data"][0]["min_temp"],
                                                                                i["forecast_data"][0]["wind_direction_desc"],
                                                                                i["forecast_data"][0]["wind_power_desc"])
                with open("city_data.txt", "a", encoding="utf-8") as fp:
                    fp.write(city_weather)
        except:
            break


