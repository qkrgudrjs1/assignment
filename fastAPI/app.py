import streamlit as st

st.title("안녕하세요 streamlit!")
st.write("안녕하세요. 여기는 텍스트 구간입니다.")

"""
# 여기는 제목
## 여기는 작은 제목
- 첫번째
- 두번째
- 새번째
"""

# 텍스트 입력상자
text = st.text_input("문자입력")
st.write(text)

# 체크박스
selected = st.checkbox("개인정보 사용에 동의하시겠습니까?")
if selected:
    st.success("동의했습니다.")

market = st.selectbox("시장", ("코스닥", "코스피", "나스닥"))
st.write(f"선택한 시장: {market}")

option = st.multiselect("종목", ["카카오", "네이버", "삼성", "LG전자"])
st.write(", ".join(option))

st.metric(label="카카오", value="30,000원", delta="5,000원")