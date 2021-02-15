#import block
import requests
import time
#main
def add_province(province_info):
    url = f'https://lab.isaaclin.cn/nCoV/api/area?latest=1&province={province_info}'
    reponse = requests.get(url)
    data = reponse.json()
    with open("nCoV.txt","a") as file:
        s = data["results"][0]["provinceName"], "的确诊人数为：", data["results"][0]["currentConfirmedCount"],"人"
        file.write(str(s))
while True:
    add_province(input(str("请输入要写入的市或省份：")))
