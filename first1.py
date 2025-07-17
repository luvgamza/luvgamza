import streamlit as st
import pandas as pd

# CSV 파일 업로드
st.title("2025년 5월 연령별 인구 현황 분석")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요 (EUC-KR 인코딩)", type="csv")

if true:
    df = pd.read_csv("CSV 파일을 업로드하세요 (EUC-KR 인코딩)", type="csv")

    # 데이터 전처리
    df["총인구수"] = df["2025년05월_계_총인구수"].astype(str).str.replace(",", "").astype(int)
    age_cols = [col for col in df.columns if col.startswith("2025년05월_계_") and "총인구수" not in col]
    new_ columns = []
    for col in age_cols:
        if '100세 이상' in col: 

    st.subheader("📋 원본 데이터 미리보기")
    st.dataframe(df)

    # 사용할 열 필터링
    age_cols = [col for col in df.columns if col.startswith("2025년05월_계_") and "총인구수" not in col]
    df = df[["행정구역", "2025년05월_계_총인구수"] + age_cols].copy()

    # 숫자형으로 변환
    df["총인구수"] = df["2025년05월_계_총인구수"].astype(str).str.replace(",", "").astype(int)
    for col in age_cols:
        df[col] = df[col].astype(str).str.replace(",", "").astype(int)

    # 열 이름에서 연령 숫자만 남기기
    new_cols = [col.replace("2025년05월_계_", "") for col in age_cols]
    df.rename(columns=dict(zip(age_cols, new_cols)), inplace=True)

    # 총인구수 상위 5개 행정구역 추출
    top5 = df.sort_values(by="총인구수", ascending=False).head(5)

    # 연령별 데이터만 전치
    age_only = top5.drop(columns=["행정구역", "2025년05월_계_총인구수", "총인구수"])
    age_only.index = top5["행정구역"]
    age_data = age_only.T

    # 인덱스 정제
    age_data.index = age_data.index.str.replace("세", "").str.replace(" ", "")
    age_data.index = age_data.index.str.replace("100세이상", "100").str.replace("100세 이상", "100").str.replace("100+", "100")
    age_data.index = age_data.index.astype(int)
    age_data.sort_index(inplace=True)

    st.subheader("📈 상위 5개 행정구역 연령별 인구 변화")
    st.line_chart(age_data)

else:
    st.warning("CSV 파일을 업로드해 주세요.")
