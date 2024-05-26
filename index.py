import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Index",
    page_icon="👋",
)
st.title("Your Digital Assistant")


if "login_status" not in st.session_state or st.session_state["login_status"] == False:
    with st.form("login"):
        st.markdown("## Login Page")
        password = st.text_input("**Password**", type = "password", autocomplete ="password")
        submit = st.form_submit_button()
        
        if submit == True and password == st.secrets["login"]:
            st.session_state["login_status"] = True
            st.rerun()
        else:
            st.session_state["login_status"] = False 
            
            if submit == True and password != st.secrets["login"]: 
                # Only display with wrong password input
                st.write(":red[Wrong password.Please try again]")

if st.session_state["login_status"] == True:
    st.toast('Successfully logged in', icon="✅")
    st.markdown("""
                ## 简单介绍
                大家好，欢迎来到我们的网站。👋
                
                我们希望透过这个项目，让你们在数码世界中遇到任何挑战，都求助有门。
                
                遇到不懂的欢迎前来询问，我们的亲切、耐心的人工智能会努力解答你的一切问题的 😀
                
                """)

    st.markdown("## 实力评估")
    level = st.radio(
        "**评估一下自己使用 ChatGPT 的实力吧，好让我们可以更好地帮你 🤗**", 
        # Radio form's title + Bold the title
        ["🟡 不懂","🟢 已入门","🔵 熟练",],
        captions = ["只能用日常语言与 ChatGPT 沟通", 
                    "懂得提示词的基本概念、有意识使用提示词", 
                    "熟练使用提示词来获取想要的回应"],
        index = None) # Set preselected option be None

    if level == "🟡 不懂":
        st.switch_page("pages/01begin.py")
    elif level == "🟢 已入门":
        st.switch_page("pages/02intermediate.py")
    elif level == "🔵 熟练":
        st.switch_page("pages/03expert.py")
        
    st.page_link("pages/04quiz.py", label="❓ 不知道自己水平？请点击这里")