import requests
import random
import os

def main():
    api_url = "https://apis.jxcxin.cn/api/mi"
    user = os.getenv("API_USER")
    password = os.getenv("API_PASSWORD")
    step = str(random.randint(40000, 50000))

    # 发起刷步请求
    response = requests.get(api_url, params={"user": user, "password": password, "step": step})

    # 解析刷步的响应
    result = response.json()

    # 输出结果
    print(result)

if __name__ == "__main__":
    main()
