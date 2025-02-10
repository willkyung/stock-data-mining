#!/usr/bin/env python
import requests
import json
import pandas as pd
from config import url, headers

# 한 번만 크롤링하는 데이터
data = {
    "isuCd": "KR7005930003",
    "isuSrtCd": "005930",
    "isuTp": "STK",
    "isuTpDtl": "undefined",
    "bld": "dbms/MDC/STAT/standard/MDCSTAT02103",
}
response = requests.post(url, headers=headers, data=data, verify=False)
stocks_json = response.json()

df = pd.DataFrame([stocks_json])
df = df[["ISU_NM", "ISU_ENG_NM", "ISU_SRT_CD", "ISU_CD", "LIST_DD"]]
df = df.rename(columns={
    "ISU_NM": "name_kr",
    "ISU_ENG_NM": "name_en",
    "ISU_SRT_CD": "code",
    "ISU_CD": "code_full",
    "LIST_DD": "listing_date"
})
df.to_csv("stocks_once.csv", index=False, encoding="utf-8-sig")



