# Connection: keep-alive
# Content-Length: 125
# sourceType: 1
# adCode: 440304
# longitude: 114.06455184
# Authorization: null
# User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1
# Content-Type: application/json
# Accept: application/json, text/plain, */*
# latitude: 22.54845664
# clientType: 7
# Origin: https://dev.ejiayou.com
# Sec-Fetch-Site: same-origin
# Sec-Fetch-Mode: cors
# Sec-Fetch-Dest: empty
# Referer: https://dev.ejiayou.com/sys/c/home?
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9
#
#     "sourceChannel": "IOS",
#     "smsCode": "666666",
#     "loginType": "BY_PHONE",
#     "phoneType": "1",
#     "phone": "13200000001",
#     "version": "6.5.8"
#
# json="loginType": "BY_PHONE","phone": "13100000003","smsCode": "666666","phoneType": "1", "sourceChannel": "H5", "machineNo": "iPhone XS Max", "apName": "易加油APP"

import datetime

time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(time)

# 这是生成报告的终端命令
# hrun.\testsuites\demo_testsuite_c.yml - -log - level debug
