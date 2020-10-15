import requests

import datetime
ti = '{dt.year}-{dt.month}-{dt.day}'.format(dt=datetime.datetime.now())
host = 'http://v.juhe.cn/calendar/day'
date = {'key': 'c6227985c9b324d2301cb5bfa91dc82d',
        'date': ti}
s = requests.post(host, data=date)
print(s.json())