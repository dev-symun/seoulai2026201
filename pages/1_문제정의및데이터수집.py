import streamlit as st
import pandas as pd

st.set_page_config(page_title="문제 정의 및 데이터 수집", page_icon="🔍")

st.title("🔍 1. 문제 정의 및 데이터 수집")
st.markdown("---")

st.markdown("""
### 🎯 1.1 문제 정의 (Problem Definition)
* **분석 배경:** 이 프로젝트를 시작하게 된 배경을 적어주세요.
* **목표:** 데이터 분석을 통해 해결하고자 하는 핵심 문제를 정의합니다.

### 📥 1.2 데이터 수집 (Data Collection)
* **데이터 출처:** (예: Kaggle, 공공데이터포털, 웹 크롤링 등)
* **데이터 명세:** 데이터의 기간, 수집 방법 등을 기록합니다.
""")

st.markdown("### 📊 수집 데이터 샘플 확인")
# 샘플 데이터 프레임 예시 (실제 데이터 로드 코드로 변경 가능)
sample_data = pd.DataFrame({
    '개인ID': [1, 2, 3, 4, 5],
    '나이': [23, 45, 31, 22, 54],
    '결제금액': [12000, 45000, 0, 150000, 32000],
    '가입일자': ['2026-01-01', '2026-01-15', '2026-02-01', '2026-03-11', '2026-05-20']
})

st.dataframe(sample_data, use_container_width=True)
st.caption("※ 위 테이블은 웹사이트 구조를 보여주기 위한 가상 데이터입니다.")
