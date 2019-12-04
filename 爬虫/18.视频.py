import requests

url = 'https://video.pearvideo.com/head/20191204/cont-1629058-14660174.mp4'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
response = requests.get(url=url,  headers=headers, verify=False).content

with open('video.mp4', 'wb') as fp:
    fp.write(response)