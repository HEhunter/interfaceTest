

import requests
import json

class RunMain():

    # def __init__(self,method,url,data):
    #     self.res = self.run_math(method,url,data)

    def send_post(self,url,data):
        res = requests.post(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def send_get(self,url,data):
        res = requests.get(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def run_math(self,method,url,data=None):
        res = None
        if method == "post":
            res =self.send_post(url, data)
        elif method == "get":
            res = self.send_get(url, data)
        return res

if __name__ == '__main__':
    url="https://www.kuaidi100.com/query?type=yunda&postid=4303562980128&temp=0.89132139814984&phone="
    data = ""
    run = RunMain().run_math("get",url=url,data=data)

    print(run)

