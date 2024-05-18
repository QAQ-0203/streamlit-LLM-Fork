import streamlit as st 
import json


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
        
