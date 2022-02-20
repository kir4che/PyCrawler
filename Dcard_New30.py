import requests

# 連上網站
forums = "sex"
url = "https://www.dcard.tw/service/api/v2/forums/" + forums + "/posts"
req = requests.get(url, headers= {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50"
})
data = req.json()

# 讀取標題與內容
for n in range(len(data)):
    print(n+1, data[n]["id"], data[n]["title"])
    try:
        post = "https://www.dcard.tw/service/api/v2/posts/" + str(data[n]["id"]) + "/comments"
        req = requests.get(post)
        comments = req.json()
        count = 0
        for count in range(len(comments)):
            print("\t" + count+1, comments[count]["content"])
    except Exception:
        print("Error")



