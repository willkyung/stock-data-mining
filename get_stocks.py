import requests
import json
import pandas as pd

def get_stocks1():
    url = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"
    headers = {
    "Accept": "*/*",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "__smVisitorID=Z-dwUA53-2H; _ga=GA1.1.490272255.1737971186; JSESSIONID=A9I4MWyirw91RZW30oak0CBhxF1nMFECpxK1DysijAoZSMTBvGABfu0eHC7K7tbI.bWRjX2RvbWFpbi9tZGNvd2FwMi1tZGNhcHAwMQ==; _ga_Z6N0DBVT2W=GS1.1.1738803742.2.0.1738803742.0.0.0",
    "Origin": "http://data.krx.co.kr",
    "Referer": "http://data.krx.co.kr/contents/MMC/RANK/rank/MMCRANK001.cmd",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    }

    data = {
    "bld": "dbms/MDC/EASY/ranking/MDCEASY01701",
    "trdDd": "20250207",
    "itmTpCd": "1",
    "mktId": "ALL",
    }

    # API 요청
    response = requests.post(url, headers=headers, data=data, verify=False)
    stocks_json = response.json()

    # JSON 데이터를 DataFrame으로 변환 후 CSV파일로 저장
    df_stock1 = pd.DataFrame(stocks_json["OutBlock_1"])
    df_stock1.to_csv("stocks1.csv", index=False, encoding="utf-8-sig")
    print("상위 50개 주식 목록")

get_stocks1()



