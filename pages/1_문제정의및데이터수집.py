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

# 제공해주신 데이터를 기반으로 샘플 데이터프레임 구성
sample_data = pd.DataFrame({
    'base_ym': [202006, 202006],
    'dpro_tgt_perd_val': [20200630, 20200630],
    'cust_ctg_type': [10001, 10001],
    'cust_class': ['C', '_'],
    'sex_type': ['F', '_'],
    'age': ['28', '_'],
    'efct_svc_count': [0, 1],
    'dt_stop_yn': ['N', 'N'],
    'npay_yn': ['N', 'N'],
    'r3m_avg_bill_amt': [2640, 300],
    'r3m_A_avg_arpu_amt': [792, 90],
    'r3m_B_avg_arpu_amt': [1584, 180],
    'r6m_A_avg_arpu_amt': [0, 0],
    'r6m_B_avg_arpu_amt': [0, 0],
    'termination_yn': ['Y', 'Y']
})

st.dataframe(sample_data, use_container_width=True)
st.caption("※ 위 테이블은 수집된 실제 데이터의 구조를 보여주는 샘플 데이터프레임입니다.")

st.markdown("""
### 📋 데이터 컬럼 명세 (Data Dictionary)
제공되거나 수집된 데이터의 각 변수(Column)에 대한 설명입니다.

| 컬럼명 (Column Name) | 설명 (Description) | 예시 데이터 |
| :--- | :--- | :--- |
| **base_ym** | 기준 년월 (Year-Month) | `202006` |
| **dpro_tgt_perd_val** | 데이터 처리 대상 기간 값 (Data Processing Target Period Value) | `20200630` |
| **cust_ctg_type** | 고객 카테고리 유형 코드 (Customer Category Type) | `10001` |
| **cust_class** | 고객 등급 / 등급 분류 (Customer Class) | `C` |
| **sex_type** | 성별 구분 (Sex Type - F: 여성, M: 남성) | `F` |
| **age** | 나이 (Age) | `28` |
| **efct_svc_count** | 유효 서비스 수 (Effective Service Count) | `0`, `1` |
| **dt_stop_yn** | 일시 정지 여부 (Date/Daily Stop Yes/No - Y/N) | `N` |
| **npay_yn** | 미납 여부 (Non-payment / Unpaid Yes/No - Y/N) | `N` |
| **r3m_avg_bill_amt** | 최근 3개월 평균 청구 금액 (Recent 3 Months Average Bill Amount) | `2640` |
| **r3m_A_avg_arpu_amt** | 최근 3개월 A 서비스 평균 ARPU (Recent 3 Months Service A Average ARPU) | `792` |
| **r3m_B_avg_arpu_amt** | 최근 3개월 B 서비스 평균 ARPU (Recent 3 Months Service B Average ARPU) | `1584` |
| **r6m_A_avg_arpu_amt** | 최근 6개월 A 서비스 평균 ARPU (Recent 6 Months Service A Average ARPU) | `0` |
| **r6m_B_avg_arpu_amt** | 최근 6개월 B 서비스 평균 ARPU (Recent 6 Months Service B Average ARPU) | `0` |
| **termination_yn** | 해지 여부 (Termination Yes/No - Y/N) | `Y` |

*※ ARPU: Average Revenue Per User (가입자당 평균 매출)*
""")
