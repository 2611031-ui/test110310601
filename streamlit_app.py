import streamlit as st

# 1. 페이지 설정 (브라우저 탭 이름과 아이콘)
st.set_page_config(page_title="내 자기소개 페이지", page_icon="👋", layout="centered")

# 2. 헤더 및 프로필 이미지
st.title("안녕하세요! 저를 소개합니다 ✨")

# 이미지가 있다면 파일명을 넣으세요. 없다면 생략 가능합니다.
# st.image("profile.jpg", width=200) 

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Profile")
    st.write("**이름:** 홍길동")
    st.write("**직업:** 데이터 분석가 / 개발자")
    st.write("**MBTI:** ENFP (아마도?)")

with col2:
    st.subheader("Contact")
    st.write("📧 Email: example@email.com")
    st.write("🔗 [GitHub](https://github.com)")
    st.write("📝 [Blog](https://velog.io)")

st.divider()

# 3. 상세 소개 (Tabs 사용)
tab1, tab2, tab3 = st.tabs(["🎯 목표", "🛠 기술 스택", "🎨 취미"])

with tab1:
    st.markdown("### 저의 비전은...")
    st.write("- 복잡한 데이터를 누구나 이해하기 쉽게 시각화하는 것을 좋아합니다.")
    st.write("- 매일 1%씩 성장하는 개발자가 되는 것이 목표입니다.")

with tab2:
    st.markdown("### 사용 가능한 도구")
    st.info("Python, Streamlit, SQL, Tableau, PyTorch")
    
    # 숙련도 표시 (Progress bar)
    st.write("Python")
    st.progress(90)
    st.write("Data Visualization")
    st.progress(85)

with tab3:
    st.markdown("### 좋아하는 것들")
    st.write("☕️ 산미 있는 아이스 아메리카노")
    st.write("🎧 로파이(Lofi) 음악 들으며 코딩하기")
    st.write("🏃 한강 러닝")

st.divider()

# 4. 방명록 기능 (간단한 인터렉션)
st.subheader("💬 응원의 한마디를 남겨주세요!")
name = st.text_input("성함/닉네임")
message = st.text_area("메시지")

if st.button("전송하기"):
    if name and message:
        st.success(f"{name}님, 소중한 의견 감사합니다! 🙌")
    else:
        st.warning("이름과 메시지를 모두 입력해주세요.")