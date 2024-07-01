import streamlit as st
from helpers.utils import evaluate_answer 

st.title("Evaluate Your Answers")  

question = st.text_input("Please Enter Your Question")
st.session_state['question'] =  question 

answer = st.text_area('Please Enter Your Answer Here',height=300)
st.session_state['answer'] = answer 

if st.button('done') : 

    output = evaluate_answer(question=st.session_state['question'] , answer= st.session_state['answer'])

    if int(output['rating']) < 5 : 
        st.header(f'Your Answer is Having Rating of :red[{output['rating']}] out of 10') 
    else : 
        st.header(f'Your Answer is Having Rating of :Green[{output['rating']}] out of 10') 

    st.divider()  
    st.header("Feedback for your Answer") 
    st.write(output['feedback'])