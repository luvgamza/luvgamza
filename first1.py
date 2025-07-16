import streamlit as st
import pandas as pd

# 파일 업로드
st.title("2025년 5월 기준 연령별 인구 현황 분석")
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요 (EUC-KR 인코딩)", type="csv")

if true:
    # CSV 파일 읽기 (EUC-KR 인코딩)
    df = pd.read_csv(uploaded_file, encoding='euc-kr')

    st.subheader("원본 데이터 미리보기")
    st.dataframe(df)

    # 열 이름 중 '2025년05월_계_'로 시작하는 열만 추출
    age_cols = [col for col in df.columns if col.startswith('2025년05월_계_')]
    age_df = df[['행정구역'] + age_cols + ['2025년05월_계_총인구수']].copy()

    # 열 이름 전처리: 연령 숫자만 남기기
    new_age_cols = [col.replace('2025년05월_계_', '') for col in age_cols]
    age_df.columns = ['행정구역'] + new_age_cols + ['총인구수']

    # '총인구수' 기준으로 상위 5개 행정구역 추출
    top5 = age_df.sort_values(by='총인구수', ascending=False).head(5)

    # 연령 데이터만 추출하여 숫자로 변환
    age_data = top5.set_index('행정구역').drop(columns='총인구수').T
    age_data.index.name = '연령'
    age_data.reset_index(inplace=True)

    # 연령을 숫자로 변환
    age_data['연령'] = age_data['연령'].str.replace('세', '').replace('100+', '100')
    age_data['연령'] = age_data['연령'].astype(int)
    age_data = age_data.sort_values(by='연령').set_index('연령')

    st.subheader("상위 5개 행정구역 연령별 인구 수")
    st.line_chart(age_data)
else:
    st.info("CSV 파일을 업로드해 주세요.")
