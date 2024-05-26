import streamlit as st 
import json
import time


def redirect():
    if st.session_state["level"][0] == "begin":
        st.switch_page("pages/01begin.py")
    elif st.session_state["level"][0] ==  "intermediate":
        st.switch_page("pages/02intermediate.py")
    elif st.session_state["level"][0] ==  "expert":
        st.switch_page("pages/03expert.py")
        
        
if "level" not in st.session_state:
    st.session_state.level = []
    
elif len(st.session_state.level) > 1:
        st.success(f" **你已经填写过了，请回到你原本的页面**",icon = "⭕")
        time.sleep(1)
        redirect()
        
else:
    with st.form("Quiz"):
        st.markdown("## 做一个小测试吧 💯")
        
        score = 0
        
        with open("quiz_question.json",encoding='utf-8') as file:
            ques=json.load(file,strict=False) # strict=False allows to store '\n','\t' etc. 
        
        for i in ("Q1","Q2","Q3","Q4","Q5","Q6"):
            #st.write(ques[i]["Choice"][1])
            question = st.radio(
                f"**{str(i)[1]} . {ques[i]["Question"]}**", 
                [ques[i]["Choice"][k] for k in range(4)],
                index = None) # Set preselected option be None
            
            ans_index = int(ques[i]["Ans"])
            if question == ques[i]["Choice"][ans_index]:
                st.write(":red[✅ 恭喜你，答对了]")
                score += 1
                
            elif question is not None:
                st.write(":grey[❌ 没关系，再接再厉]")
                st.markdown(f'正确答案是 **{ques[i]["Choice"][ans_index]}**')
                     
                
            st.divider()
        
                
        if  st.form_submit_button("递交", type = "primary") == True:         
            
            st.subheader(f":blue[你的分数：**{score}**]")
        
            if score >= 5:
                st.page_link("pages/03expert.py", label="**你已经是熟练级别了**")
                st.session_state.level.append("expert")
                
            elif score >=3 :
                st.page_link("pages/02intermediate.py", label="**你已经到了已入门级别了**")
                st.session_state.level.append("intermediate")
                
            elif score >=0:
                st.page_link("pages/01begin.py", label="**你看来不是很熟悉大语言模型了**")
                st.session_state.level.append("begin")

            st.toast("请点击按钮跳转到指定页面，否则将在 10 秒后自动跳转",icon = "💬")
            
            time.sleep(10)
            redirect()