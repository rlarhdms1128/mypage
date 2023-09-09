import streamlit as st
from PIL import Image
st.set_page_config(
        page_title= '하이',
        page_icon = 'ㅇㅇ'
)
menu = st. selectbox('MENU',['자기소개','학교소개','동아리소개','관심분야'])
if menu == '자기소개':
    st.subheader('자기소개')
        
elif menu == '학교소개':
    st.subheader('학교소개')

    image = Image.open("매천고등학교.jpg")
    st.image(image, caption="매천고등학교")
    st.write("제가 다니는 매천고등학교는 대구 북구에 위치한 고등학교 입니다!")
    st.write("참고로 매천고는 매일 천개의 꿈이 영그는 고품격학교.....라는 뜻이 있다고 합니다..")
    image = Image.open("ai 중심.png")
    st.image(image, caption="ai 융합교육 중심")
    st.write("저희 학교는 AI융합교육 중심 고등학교로 관련된 다양한 경험을 할 수 있습니다")
    st.write("이 분야에 관심이 있는 학생은 더욱 도움을 많이 받을 수 있습니다.")
    image = Image.open("도서관.png")
    st.image(image, caption="도서관")
    st.write("깔끔하고 편안한 도서관이 있어 학생들이 애용합니다")
    image = Image.open("크롬북.jpg")
    st.image(image, caption="실제 크롬북 사용 사진")
    st.write("저희 학교는 각 학생들에게 크롬북을 하나씩 제공합니다")
    st.write("학생들은 수행평가나 학교활동에 부담없이 잘 활용합니다.")

elif menu == '동아리소개':
    st.subheader('동아리소개')
    st.write("제가 현재 소속한 동아리는 소프트웨어 동아리 입니다.")
    st.write("참고로 현재 수업을 해주시는 마호돌 선생님 께서 맡아주시고 계십니다.")
    image = Image.open("동아리.jpg")
    st.image(image, caption="동아리 홍보 포스터")
    st.write("저희 동아리는 게임개발과 웹개발로 나뉘어 각자 활동을 합니다.")
    st.write("그래서 프로그램 중에서도 더 자신에게 맞는 활동을 선택 할 수 있습니다.")
    image = Image.open("동아리활동.jpg")
    st.image(image, caption="동아리 활동 중 사진")
    st.write("저는 현재 웹개발팀에서 동아리 활동을 하고 있습니다.")
    st.write("현재는 streamlit 등을 활용하여 실용적인 활동을 합니다.")
else:
    st.subheader('관심분야')
    st.write("제 관심 분야는 웹개발이고 현제 컴퓨터공학과 진학을 희망하고 있습니다.")
    st.write("그래서 1학년 때 부터 관련 활동을 많이 하기 위해 노력 하고 있습니다.")
    st.write("저는 1학년 때 인공지능 개발 동아리에서도 다양한 경험을 했습니다.")
    image = Image.open("1학년동아리1.jpg")
    st.image(image, caption="동아리 활동 중 사진")
    st.write("위 사진은 움직이는 울타리 보호대를 만들기 위해 아두이노와 초음파 센서를 이용하는 모습입니다.")
    st.write("2학년에 올라와서도 다양한 경험을 했는데")
    st.write("그 중 가장 기억에 남는 활동은 바로 소인수 수업입니다")
    st.write("저는 빅데이터 분석이라는 소인수 수업을 들었는데")
    st.write("거기서 상권 분석을 통해 창업 계획을 세워보기도 했습니다.")
    st.write("아래 사진은 위 주제에 관한 발표자료인데")
    image = Image.open("소인수.png")
    st.image(image, caption="소인수 수업 발표 자료")
    st.write("저 초록색 그래프는 대구의 분야별 상점 수를 분석하여 시각화 한 것 입니다")
