import streamlit as st
import json 
from helpers.utils import * 

category_list = {   None : None,
                    'MCQ' : generate_mcqs , 
                    'Multiple choices' : generate_multiple_ans_mcqs,
                    'true or false' : generate_true_false,
                    'short answer question' : generate_sort_answer_questins,
                    'long answer question':generate_long_question_answer,
                    'fill in the blank':generate_fill_in_the_blank,
                    'Problem solving question':generate_probem_solving_questions,
                    'scenario question': generate_senario_based_questions,
                    'linking choices question': generate_case_study_questions,
                    'coding question' : generate_coding_questions,}


selective_questions_list = list(JSON_FORMATS.keys())
selective_questions = ['Problem solving question','scenario question','linking choices question']

st.header('Please Select 3 types of teh question Questions :')
st.divider()

first_question = st.selectbox('1 Question',list(category_list.keys()))
st.session_state['first_question'] = first_question 

if first_question in  selective_questions:

    first_question_type = st.selectbox(':green[Please Enter 1st Question Type]',selective_questions_list) 
    st.session_state['first_question_type'] = first_question_type 
    
    first_question_domain = st.text_input('Please Enter :red[Domain Name]',) 
    st.session_state['first_question_domain'] = first_question_domain 
    
    first_question_difficulty = st.text_input("Please Enter Difficulty Level For Given Question")
    st.session_state['first_question_difficulty'] = first_question_difficulty  

    first_question_nums = st.number_input('Please Enter :blue[Number of Question] you want')
    st.session_state['first_question_nums'] = first_question_nums

    if st.button('Proceed'):
        with st.spinner("Generating...") : 
            first_question_output = category_list[first_question](st.session_state['first_question_domain'],st.session_state['first_question_difficulty'],st.session_state['first_question_nums'],st.session_state['first_question_type'])
            st.session_state['first_question_output'] = first_question_output
    st.divider() 

else : 
    if first_question is not None : 
        first_question_domain = st.text_input('Please Enter :red[Domain Name]',) 
        st.session_state['first_question_domain'] = first_question_domain 
        
        first_question_difficulty = st.text_input("Please Enter Difficulty Level For Given Question : [easy, medium, hard, extreme]")
        st.session_state['first_question_difficulty'] = first_question_difficulty  

        first_question_nums = st.number_input('Please Enter :blue[Number of Question] you want')
        st.session_state['first_question_nums'] = first_question_nums

        if st.button('Proceed'):
            with st.spinner("Generating ...") : 
                first_question_output = category_list[first_question](st.session_state['first_question_domain'],st.session_state['first_question_difficulty'],st.session_state['first_question_nums'])
                st.session_state['first_question_output'] = first_question_output
    
st.divider() 

second_question = st.selectbox('2 Question',list(category_list.keys()))
st.session_state['second_question'] = second_question 

if second_question in  selective_questions:
    
    second_question_type = st.selectbox(':green[Please   Enter   1st Question Type]',selective_questions_list) 
    st.session_state['second_question_type'] = second_question_type 
    
    second_question_domain = st.text_input('Please   Enter :red[Domain Name]',) 
    st.session_state['second_question_domain'] = second_question_domain 
    
    second_question_difficulty = st.text_input("Please   Enter Difficulty   Level For Given Question ")
    st.session_state['second_question_difficulty'] = second_question_difficulty  

    second_question_nums = st.number_input('Please Enter :blue[Number of   Question] you want')
    st.session_state['second_question_nums'] = second_question_nums

    if st.button('Proceed..'):
        with st.spinner("Generating  ...") : 
            second_question_output = category_list[second_question](st.session_state['second_question_domain'],st.session_state['second_question_difficulty'],st.session_state['second_question_nums'],st.session_state['second_question_type'])
            st.session_state['second_question_output'] = second_question_output
    st.divider() 

else : 
    if second_question is not None : 
        second_question_domain = st.text_input('Please  Enter :red[Domain   Name]',) 
        st.session_state['second_question_domain'] = second_question_domain 
        
        second_question_difficulty = st.text_input(" Please Enter Difficulty  Level For Given   Question")
        st.session_state['second_question_difficulty'] = second_question_difficulty  

        second_question_nums = st.number_input(' Please Enter :blue[Number of Question] you  want')
        st.session_state['second_question_nums'] = second_question_nums

        if st.button('Proceed  '):
            with st.spinner("Generating...") : 
                second_question_output = category_list[second_question](st.session_state['second_question_domain'],st.session_state['second_question_difficulty'],st.session_state['second_question_nums'])
                st.session_state['second_question_output'] = second_question_output
    
st.divider() 

third_question = st.selectbox('3 Question',list(category_list.keys()))
st.session_state['third_question'] = third_question 

if third_question in  selective_questions:

    
    third_question_type = st.selectbox(':green[Please Enter 1st Question Type]',selective_questions_list) 
    st.session_state['third_question_type'] = third_question_type 
    
    third_question_domain = st.text_input('Please Enter :red[Domain Name]',) 
    st.session_state['third_question_domain'] = third_question_domain 
    
    third_question_difficulty = st.text_input("Please Enter Difficulty Level For Given Question")
    st.session_state['third_question_difficulty'] = third_question_difficulty  

    third_question_nums = st.number_input('Please Enter :blue[Number of Question] you want')
    st.session_state['third_question_nums'] = third_question_nums

    if st.button('Proceed'):
        with st.spinner("Generating...") : 
            third_question_output = category_list[third_question](st.session_state['third_question_domain'],st.session_state['third_question_difficulty'],st.session_state['third_question_nums'],st.session_state['third_question_type'])
            st.session_state['third_question_output'] = third_question_output
    st.divider() 

else : 
    if third_question is not None : 
        third_question_domain = st.text_input('Please Enter: :red[Domain Name]',) 
        st.session_state['third_question_domain'] = third_question_domain 
        
        third_question_difficulty = st.text_input("Please  Enter Difficulty Level For   Given Question  ")
        st.session_state['third_question_difficulty'] = third_question_difficulty  

        third_question_nums = st.number_input('Please   Enter :blue[Number of Question]  you   want')
        st.session_state['third_question_nums'] = third_question_nums

        if st.button('Proceed.'):
            with st.spinner("Generating...") : 
                third_question_output = category_list[third_question](st.session_state['third_question_domain'],st.session_state['third_question_difficulty'],st.session_state['third_question_nums'])
                st.session_state['third_question_output'] = third_question_output
    
st.divider() 

if st.button("Output"): 
    st.header("1st Question's Output")
    st.divider()
    st.write(st.session_state['first_question_output']) 
    st.divider() 
    st.header("2nd Question's Output")
    st.divider() 
    st.write(st.session_state['second_question_output'])
    st.divider()
    st.header("3rd Question's Output")
    st.divider() 
    st.write(st.session_state['third_question_output']) 
