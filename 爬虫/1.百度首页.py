# import requests
#
# #  请求地址
# # url = "https://www.baidu.com/"
# url = "https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6%E7%9A%84%E6%81%90%E6%80%96&oq=%25E9%2587%258F%25E5%25AD%2590%25E5%258A%259B%25E5%25AD%25A6%25E7%259A%2584%25E6%2581%2590%25E6%2580%2596&rsv_pq=902ce07b00020c35&rsv_t=02aazqYkiqKhnikQ8I7PzfxgNlsF1tcX84RZJyaHOxq7tP1E8tGUftj5RXI&rqlang=cn&rsv_enter=0&rsv_dl=ts_0&prefixsug=%25E9%2587%258F%25E5%25AD%2590%25E5%258A%259B%25E5%25AD%25A6%25E7%259A%2584%25E6%2581%2590%25E6%2580%2596&rsp=0&rsv_sug9=es_0_1&rsv_sug=5"
#
# #  请求方式: method:Get ,post
# #  做伪装:添加headers
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
# #  发起请求,返回响应
# response = requests.get(url=url, headers=headers)
#
# print(response)
#
# #  查看响应内容
# #  response.text : 返回文本信息:
# # print(response.text)
# #  response.content: 返回字节流信息 :  + encode()
# print(response.content.decode('utf-8'))
#
# #  写入本地文件
# with open('baidu.html', 'w', encoding='utf-8' ) as fp:
#     fp.write(response.content.decode('utf-8'))
import time

now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(now_time)