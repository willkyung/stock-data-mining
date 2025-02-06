import requests
from config import url,headers,cookies,data

response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False)

# 한글 인코딩 문제 해결
print(response.text)



# 상위 50개 이름들 가져오기
# 상장일, 