#!/usr/bin/env python
import requests
import json
import pandas as pd
from datetime import datetime
from config import url, headers

# 매일 크롤링하는 데이터
data = {
    "isuCd": "KR7005930003",
    "isuSrtCd": "005930",
    "isuTp": "STK",
    "isuTpDtl": "undefined",
    "bld": "dbms/MDC/STAT/standard/MDCSTAT02101",
}
response = requests.post(url, headers=headers, data=data, verify=False)
stocks_json = response.json()

df = pd.DataFrame([stocks_json])
df = df[["PRSNT_PRC", "FLUC_RT", "ACC_TRDVOL", "ACC_TRDVAL"]]
df = df.rename(columns={
    "PRSNT_PRC": "price",
    "FLUC_RT": "change",
    "ACC_TRDVOL": "volume",
    "ACC_TRDVAL": "trade_value"
})

df["date"] = datetime.now().strftime("%Y-%m-%d")
df.to_csv("stocks_daily.csv", index=False, encoding="utf-8-sig")






