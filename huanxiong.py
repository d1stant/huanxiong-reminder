import requests

token = ""
cookie = ""
headers = {
    "authority": "sxkjep.mrrac.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5",
    "api-version": "1.0.0",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "eagleeye-pappname": "hy78v40gt0@7b1387d125865d8",
    "eagleeye-sessionid": "ydl8hn3Xq1y4hvrwmsRadC9vUaL2",
    "eagleeye-traceid": "136e5a8a16972936646911009865d8",
    "from-agent": "SxkjPhone",
    "origin": "https://sxkjep.mrrac.com",
    "pragma": "no-cache",
    "referer": "https://sxkjep.mrrac.com/pages/myOrder/myOrder",
    "sec-ch-ua": '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "token": token,
    "Cookie": cookie,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
}


def loadOrderList():
    url = "https://sxkjep.mrrac.com/api/order/loadOrderList"
    params = {"type": "1", "year": "2023", "month": "10", "model": "0"}
    data = {}
    req = requests.post(url, params=params, headers=headers, data=data)
    print(req.text)


def loadUserOrderDetails(order_id: str):
    url = "https://sxkjep.mrrac.com/api/order/loadUserOrderDetails"
    params = {"id": order_id, "model": "0"}
    # params = {"id": "35244348", "model": "0"}
    data = {}
    req = requests.post(url, params=params, headers=headers, data=data)
    print(req.text)
