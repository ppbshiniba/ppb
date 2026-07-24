import streamlit as st

st.set_page_config(
    page_title="拯救者联盟简介",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://7921.e73k.com/enter/index.html',
        'Report a bug': "https://7921.e73k.com/enter/index.html",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

#标题
st.title("拯救者联盟")

st.header("四人组")
st.subheader("一般以以下形式出现")

st.write("四人组里面一般至少有一个神人")
st.write("qio是一种类人猿，由于其温顺的性格被誉为人类最好的炮友")
st.write("它们体型较大，长大后可到达100kg~150kg不等，被誉为类人猿界的“良子”")
st.write("它在最早期时由于同类之间存在生殖隔离，选择与猿类联姻，以下是珍贵图片")

st.image("b.jpg")

st.write("由于当时人类并没有发明出雨伞，所以也是有了这么一张令人看了怜爱的照片")
st.image("c.jpg")

st.write("四人组一般有一个逗比")
st.write("卢康，网名落阔，自诩为“艾希迪克”，此人爱好健身，但是有健身人士的通病，就是头脑简单四肢发达")
st.write("一次，由于第一次发现QQ有神奇的特效，所以高兴得吐出了舌条，这是珍贵记录")
st.image("d.jpg")

