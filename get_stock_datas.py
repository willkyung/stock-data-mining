# name_kr(국문명): 1페이지 - ISU_ABBRV, 2페이지 - ISU_NM
# name_en(영문명): 2페이지 - ISU_ENG_NM
# code(계열사코드): 1페이지 - ISU_CD, 2페이지 - ISU_SRT_CD
# code_full(회사코드): 1페이지 - ISU_CD_FULL, 2페이지 - ISU_CD
# listing_date(상장일): 2페이지 - LIST_DD 
# date(날짜): 2페이지 - wdDd 
# price(종가): 1페이지 - TDD_CLSPRC, 2페이지 - PRSNT_PRC 
# change(종가의 전일 대비 변화율): 1페이지 - FLUC_RT, 2페이지 - FLUC_RT  => 종가의 전일 대비 변화량으로 할거면 CMPPREVDD_PRC(1, 2페이지 동일)
# volume(거래량): 1페이지 - ACC_TRDVOL, 2페이지 - ACC_TRDVOL
# trade_value(거래대금): 1페이지 - ACC_TRDVAL , 2페이지 - ACC_TRDVAL 
# total_shares(상장주식수): 1페이지 - LIST_SHRS, 2페이지 - LIST_SHRS 
# per(주가수익비율): 2페이지 - PER
# pbr(주가순자산비율): 2페이지 - PBR
# div_yield(배당수익률): 2페이지 - DIV_YD 
# foreign_ratio(외국인 보유 비율): 2페이지 - FORN_RTO

import requests
import json
import pandas as pd

def get_stock_datas1():

    url = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"

    headers = {
    "Accept": "*/*",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "__smVisitorID=D5EJpXcZyJF; JSESSIONID=iTEaaaDE00qSgveUMuS0vVu4kn095s6mv9nC6jFCVyV0lRPyvc3VaKJVtLZZRqmN.bWRjX2RvbWFpbi9tZGNvd2FwMS1tZGNhcHAxMQ==",
    "Origin": "http://data.krx.co.kr",
    "Referer": "http://data.krx.co.kr/contents/MMC/ISIF/isif/MMCISIF003.cmd?tabIndex=0&isuCd=KR7005930003&isuSrtCd=005930&isuTp=STK&isuTpDtl=undefined&prodId=undefined",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    }

    data = {
    "isuCd": "KR7005930003",
    "isuSrtCd": "005930",
    "isuTp": "STK",
    "isuTpDtl": "undefined",
    "bld": "dbms/MDC/STAT/standard/MDCSTAT02101",
    }

    # API 요청
    response = requests.post(url, headers=headers, data=data, verify=False)
    stocks_json = response.json()

    # JSON 데이터를 DataFrame으로 변환 후 CSV파일로 저장
    df_stock2 = pd.DataFrame([stocks_json]) 
    df_stock2.to_csv("stocks2.csv", index=False, encoding="utf-8-sig")

def get_stock_datas2():

    url = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"

    headers = {
    "Accept": "*/*",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "__smVisitorID=D5EJpXcZyJF; JSESSIONID=iTEaaaDE00qSgveUMuS0vVu4kn095s6mv9nC6jFCVyV0lRPyvc3VaKJVtLZZRqmN.bWRjX2RvbWFpbi9tZGNvd2FwMS1tZGNhcHAxMQ==",
    "Origin": "http://data.krx.co.kr",
    "Referer": "http://data.krx.co.kr/contents/MMC/ISIF/isif/MMCISIF003.cmd?tabIndex=0&isuCd=KR7005930003&isuSrtCd=005930&isuTp=STK&isuTpDtl=undefined&prodId=undefined",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    }

    data = {
    "isuCd": "KR7005930003",
    "isuSrtCd": "005930",
    "isuTp": "STK",
    "isuTpDtl": "undefined",
    "bld": "dbms/MDC/STAT/standard/MDCSTAT02103",
    }

    # API 요청
    response = requests.post(url, headers=headers, data=data, verify=False)
    stocks_json = response.json()

    # JSON 데이터를 DataFrame으로 변환 후 CSV파일로 저장
    df_stock3 = pd.DataFrame([stocks_json]) 
    df_stock3.to_csv("stocks3.csv", index=False, encoding="utf-8-sig")

def merge_df():
    try:
        # CSV 파일을 다시 불러와서 병합
        df_stock2 = pd.read_csv("stocks2.csv", encoding="utf-8-sig")
        df_stock3 = pd.read_csv("stocks3.csv", encoding="utf-8-sig")

        df_merged = pd.concat([df_stock2, df_stock3], axis=1)  # 열 방향으로 병합

        # 중복 컬럼 제거
        df_merged = df_merged.loc[:, ~df_merged.columns.duplicated()]

        # 필요한 열만 추출 
        df = df_merged[["ISU_NM", "ISU_ENG_NM", "ISU_SRT_CD", "ISU_CD", "LIST_DD", "wdDd", "PRSNT_PRC", "FLUC_RT", "ACC_TRDVOL", "ACC_TRDVAL", "LIST_SHRS", "PER", "PBR", "DIV_YD", "FORN_RTO"]]  
        df_final = df.rename(columns = {
            "ISU_NM": "name_kr", 
            "ISU_ENG_NM": "name_en",
            "ISU_SRT_CD": "code", 
            "ISU_CD": "code_full", 
            "LIST_DD": "listing_date", 
            "wdDd": "date", 
            "PRSNT_PRC": "price", 
            "FLUC_RT": "change", 
            "ACC_TRDVOL": "volume", 
            "ACC_TRDVAL": "trade_value", 
            "LIST_SHRS": "total_shares", 
            "PER": "per", 
            "PBR": "pbr", 
            "DIV_YD": "div_yield", 
            "FORN_RTO": "foreign_ratio"
        })

        # CSV 파일로 저장
        df_final.to_csv("stocks_final.csv", index=False, encoding="utf-8-sig")
        print("병합된 데이터 저장 완료: stocks_final.csv")

    except Exception as e:
        print("merge_df() 실행 중 오류 발생:", e)

get_stock_datas1()
get_stock_datas2()
merge_df()






