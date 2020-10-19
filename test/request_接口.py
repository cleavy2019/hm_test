import requests

bar = {"city": "西安",
       "key": "2a20b03607084fb48043b367437ca5de"}
r = requests.get("http://apis.juhe.cn/simpleWeather/query", params=bar)
print(r.json())

bar1 = {"key": "4e522b9480ef8394c0799c7808878ad4",
        "sort": "asc",
        "time": "1418816972"}
r1 = requests.post("http://v.juhe.cn/joke/content/list.php", data=bar1)
print(r1.json())




