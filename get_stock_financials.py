#!/usr/bin/env python
import requests
import json
import pandas as pd
from datetime import datetime
from config import url, headers

# 일주일에 한번 크롤링하는 데이터
# 첫 번째 요청 (LIST_SHRS 관련 데이터)
data1 = {
    "isuCd": "KR7005930003",
    "isuSrtCd": "005930",
    "isuTp": "STK",
    "isuTpDtl": "undefined",
    "bld": "dbms/MDC/STAT/standard/MDCSTAT02103",
}
response1 = requests.post(url, headers=headers, data=data1, verify=False)
stocks_json1 = response1.json()

# 두 번째 요청 (PER, PBR, DIV_YD, FORN_RTO 관련 데이터)
data2 = {
    "isuCd": "KR7005930003",
    "isuSrtCd": "005930",
    "isuTp": "STK",
    "isuTpDtl": "undefined",
    "bld": "dbms/MDC/STAT/standard/MDCSTAT02101",
}
response2 = requests.post(url, headers=headers, data=data2, verify=False)
stocks_json2 = response2.json()

# 첫 번째 요청 데이터를 DataFrame으로 변환
df1 = pd.DataFrame([stocks_json1])
df1 = df1[["LIST_SHRS"]]
df1 = df1.rename(columns={
    "LIST_SHRS": "total_shares"
})

# 두 번째 요청 데이터를 DataFrame으로 변환
df2 = pd.DataFrame([stocks_json2])
df2 = df2[["PER", "PBR", "DIV_YD", "FORN_RTO"]]
df2 = df2.rename(columns={
    "PER": "per",
    "PBR": "pbr",
    "DIV_YD": "div_yield",
    "FORN_RTO": "foreign_ratio"
})

# 두 데이터프레임 병합
df = pd.concat([df1, df2], axis=1)
df["date"] = datetime.now().strftime("%Y-%m-%d")

# CSV 파일로 저장
df.to_csv("stocks_weekly.csv", index=False, encoding="utf-8-sig")


