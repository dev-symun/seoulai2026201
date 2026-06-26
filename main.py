import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="데이터 분석 프로젝트 대시보드",
    page_icon="📊",
    layout="wide"
)

# 메인 타이틀
st.title("📊 문서연의 메인 홈")
st.subheader("웹사이트에 오신 것을 환영합니다!")

st.markdown("---")

# 프로젝트 소개
st.markdown("""
### 💡 프로젝트 개요
이 웹애플리케이션은 데이터 수집부터 전처리, 시각화, 그리고 머신러닝 모델링까지의 **전체 데이터 분석 프로세스**를 보여주기 위해 제작되었습니다.

왼쪽 사이드바의 메뉴를 이용해 각 단계별 분석 결과를 확인해보세요!
""")

# 파이프라인 안내 (Visual Guide)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.info("**1. 문제 정의 & 수집**\n\n프로젝트 목표 및 데이터셋 소개")
with col2:
    st.success("**2. 데이터 전처리**\n\n결측치 처리 및 데이터 정제")
with col3:
    st.warning("**3. 데이터 시각화**\n\nEDA 및 인사이트 도출")
with col4:
    st.error("**4. AI 모델링**\n\n모델 학습 및 성능 평가")
