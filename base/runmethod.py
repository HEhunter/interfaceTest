#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__: hunter

import requests
import json


class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header).json()
        else:
            res = requests.post(url=url, data=data).json()
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)

    def get_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res.text

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)


if __name__ == "__main__":
    url = "https://www.juhe.cn/login/login"
    data = {
        "username": "18216426224",
        "password": "tOqPBxJt4ZfMyZ3lsP+MSpfEq5DOwwVbdu4+2USVF//EmcxjzQxXNR9lkHnz3HGkMUiR3D7Uc5qXv3axQvoyFwHiKVihSsY+NJW9Jz6PBr4KzSLhsfq0BbF5QiXMj3K6bIjbDMD6A/8JOgBxkegpVkN2WFSxKbC8uxIXYJ18CP5N9LJI+7U7Wcs1syJqju1Wz5vwBSu71wL1cRocw9ODV2gri4RByy0/W5/cwREibZCeA64sLCfRdfxSN9HZeRG6mujsllHe7csbOXtSSTkgGWRfLpG0ePol4/9BZX2vkLUME+f1SNaNkSQFgQGUiqJphP5HNIPhDly5SZsBSMTjVA==",
        "secondMobile": "",
        "secondCode": "",
        "captcha": "",
        "uuid": ""
    }
    run = RunMethod()
    print(run.run_main("post", url, data))
    for i in range(1, 3):
        print(i)
