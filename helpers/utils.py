import os 
import google.generativeai as gen_ai 
import json 
from dotenv import load_dotenv 
load_dotenv()  

GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
gen_ai.configure(api_key= GOOGLE_API_KEY)
Gemini_Pro = gen_ai.GenerativeModel('gemini-pro')

MAX_RETRY = 3 
JSON_FORMATS = {None : None , 
                'mcqs':'''  {questions :{question_1 : "....." , 
                                        question_2 : "....." , 
                                            .
                                        question_N : "......" }  , 
                                        
                            options :{ question_1 :{ A: "abc" , B: "xyz" , C: "def" , D: "uvw" , } ,
                                        question_2 : { A: "abc" , B: "xyz" , C: "def" , D: "uvw" , } ,
                                             .
                                        question_N : { A: "abc" , B: "xyz" , C: "def" , D: "uvw" , },} , 
                            
                            answers : { answer_1 : {C : "def" } , 
                                        answer_2 : {A : "abc" } ,
                                            . 
                                        answer_N : {D: "uvw"} , } } ''' , 

        'multiple_choise_mcqs' :'''{ questions : {  question_1 : "....." , 
                                                    question_2 : "....." , 
                                                        .
                                                    question_N : "......" }  , 
                                                
                                                options : { question_1 : { A: "..." , B: "..." , C: "..." , D: "..." , } ,
                                                            question_2 : { A: "..." , B: "..." , C: "..." , D: "..." , } ,
                                                            .
                                                            question_N : { A: "..." , B: "..." , C: "..." , D: "..." , },
                                                        } , 
                                                answers : { answer_1 : {B : "...." ,D: "...." } , 
                                                            answer_2 : {A : "...." ,D: "...."} , 
                                                            answer_2 : {C : "...." } , 
                                                            . 
                                                            answer_N : {B: ".....", C: "....",} , } }''' , 

        'true_false' : '''{ questions :{question_1 : "....." ,
                                        question_2 : "....." , 
                                        .
                                        question_N : "....." }  , 
            
                            answers : { answer_1 : {ans : True } , 
                                        answer_2 : {ans : False } , 
                                        . 
                                        answer_N : {ans : False , }''', 

        'sort_answers': '''  {  questions : {   question_1 : "....." , 
                                                question_2 : "....." , 
                                                .
                                                question_N : "......" }  , 

                                hints : {   hint_1 : {hint : "...." } , 
                                            hint_2 : {hint : "...." } ,  
                                            . 
                                            hint_N : {hint : "....."} , } }''',

        'fill_the_blanks' : '''    { questions : {  question_1 : "....." , 
                                                    question_2 : "....." , 
                                                    .
                                                    question_N : "......" }  , 
                            
                                    blanks : {  blank_1 : {ans : "...." } , 
                                                blank_2 : {ans : "...." } , 
                                                . 
                                                blank_N : {ans : "...." , } }''', } 

def generate_mcqs(Domain_name: str, difficulty_level:str ,num_questions: int = 10): 
    
    prompt = f''' 
    Please generate {num_questions} multiple choice questions within the domain of {Domain_name}
    Each question should have four possible answers (A, B, C, and D), 
    with only one correct answer. and Difficulty Level should be {difficulty_level}
    Provide the questions and answers in the following JSON format:
    
    outpt should be in this below format :

    Structured output Format : 

    {JSON_FORMATS.get('mcqs')} 

    The JSON string should be valid and properly formatted to allow for JSON parsing using `json.loads(json_string)`. 
    Only provide the JSON string in the output, without any additional text or explanation '''
    
    retry  =  0
    while retry < MAX_RETRY : 
            try : 
                given_string = Gemini_Pro.generate_content(prompt).text          
                json_string =given_string[given_string.find('{'):given_string.rfind('}') + 1]
                json_objects = json.loads(json_string)
                return json_objects 
            
            except : 
                retry += 1

def generate_true_false(Domain_name: str, difficulty_level:str ,num_questions: int = 10): 
        
    prompt = f''' 
    Please generate {num_questions} True False questions within the domain of {Domain_name}
    Each question should have 2 possible answers True and False 
    with only one correct answer. and difficulty Level Should be : {difficulty_level} 

    Provide the questions and answers in the following JSON format:
    
    outpt should be in this below format :

    Structured output Format : 

    {JSON_FORMATS.get('true_false')} 

    The JSON string should be valid and properly formatted to allow for JSON parsing using `json.loads(json_string)`. 
    Only provide the JSON string in the output, without any additional text or explanation '''

    retry  =  0
    while retry < MAX_RETRY : 
            try : 
                given_string = Gemini_Pro.generate_content(prompt).text          
                json_string =given_string[given_string.find('{'):given_string.rfind('}') + 1]
                json_objects = json.loads(json_string)
                return json_objects 
            
            except : 
                retry += 1

def generate_multiple_ans_mcqs(Domain_name: str, difficulty_level:str ,num_questions: int = 10): 
    
    prompt = f''' 
    Please generate {num_questions} multiple choice and multiple answered questions within the domain of {Domain_name}
    Each question should have four possible answers (A, B, C, and D), 
    with only one correct or more correct answers.. 

    Difficulty Level for Qeustions shole be : {difficulty_level} 
    Provide the questions and answers in the following JSON format:
    
    outpt should be in this below format :

    Structured output Format : 

    {JSON_FORMATS.get('multiple_choise_mcqs')} 

    The JSON string should be valid and properly formatted to allow for JSON parsing using `json.loads(json_string)`. 
    Only provide the JSON string in the output, without any additional text or explanation '''

    retry  =  0
    while retry < MAX_RETRY : 
            try : 
                given_string = Gemini_Pro.generate_content(prompt).text          
                json_string =given_string[given_string.find('{'):given_string.rfind('}') + 1]
                json_objects = json.loads(json_string)
                return json_objects 
            
            except : 
                retry += 1

def generate_sort_answer_questins(Domain_name: str , difficulty_level:str,num_questions: int = 10):

    prompt = f''' 
    Please generate {num_questions} short answerd questions ( questions which don't have answer more then 3 lines) the domain of {Domain_name}
    Each question should have one hint.. 

    and Difficulty Level For Qeustions should be : {difficulty_level} 
    Provide the questions and it's hint in the following JSON format:
    
    outpt should be in this below format :

    Structured output Format : 

    {JSON_FORMATS.get('sort_answers')} 

    The JSON string should be valid and properly formatted to allow for JSON parsing using `json.loads(json_string)`. 
    Only provide the JSON string in the output, without any additional text or explanation '''

    retry  =  0
    while retry < MAX_RETRY : 
            try : 
                given_string = Gemini_Pro.generate_content(prompt).text          
                json_string =given_string[given_string.find('{'):given_string.rfind('}') + 1]
                json_objects = json.loads(json_string)
                return json_objects 
            
            except : 
                retry += 1

def generate_long_question_answer(Domain_name: str , difficulty_level:str,num_questions: int = 10):

    prompt = f''' 
    Please generate {num_questions} short answerd questions ( questions which have answer of more than 5 to 6 lines ) the domain of {Domain_name}
    Each question should have one hint.. 

    and Difficulty Level For Qeustions should be : {difficulty_level} 
    Provide the questions and it's hint in the following JSON format:
    
    outpt should be in this below format :

    Structured output Format : 

    {JSON_FORMATS.get('sort_answers')} 

    The JSON string should be valid and properly formatted to allow for JSON parsing using `json.loads(json_string)`. 
    Only provide the JSON string in the output, without any additional text or explanation '''
    
    retry  =  0
    while retry < MAX_RETRY : 
            try : 
                given_string = Gemini_Pro.generate_content(prompt).text          
                json_string =given_string[given_string.find('{'):given_string.rfind('}') + 1]
                json_objects = json.loads(json_string)
                return json_objects 
            
            except : 
                retry += 1 

def generate_fill_in_the_blank(Domain_name: str, difficulty_level:str ,num_questions: int = 10): 
        
    prompt = f''' 
    Please generate {num_questions} feel In the Blank the domain of {Domain_name}
    Each question should have one Correct answer as the fill of the given blank 
    and difficulty Level Should be : {difficulty_level} 

    Provide the questions and answers in the following JSON format:
    
    outpt should be in this below format :

    Structured output Format : 

    {JSON_FORMATS.get('multiple_choise_mcqs')} 

    The JSON string should be valid and properly formatted to allow for JSON parsing using `json.loads(json_string)`. 
    Only provide the JSON string in the output, without any additional text or explanation '''

    retry  =  0
    while retry < MAX_RETRY : 
            try : 
                given_string = Gemini_Pro.generate_content(prompt).text          
                json_string =given_string[given_string.find('{'):given_string.rfind('}') + 1]
                json_objects = json.loads(json_string)
                return json_objects 
            
            except : 
                retry += 1

def generate_linking_choise_questions(Domain_name: str, difficulty_level:str ,num_questions: int = 10): 
        
    prompt = f''' 
    Please generate {num_questions} Linking Choices Questions ( Linking choices questions often include a blank, 
    which indicates where the chosen word or phrase should be inserted to create a logical connection between ideas or sentences ) 
    
    The domain of {Domain_name}

    Each question should have four possible answers for Given Blank which are (A, B, C, and D), 
    and thare is one correct answer for Given Blank.

    and difficulty Level Should be : {difficulty_level} 

    Provide the questions and answers in the following JSON format:
    
    outpt should be in this below format :

    Structured output Format : 

    {JSON_FORMATS.get('mcqs')} 

    The JSON string should be valid and properly formatted to allow for JSON parsing using `json.loads(json_string)`. 
    Only provide the JSON string in the output, without any additional text or explanation '''

    retry  =  0
    while retry < MAX_RETRY : 
            try : 
                given_string = Gemini_Pro.generate_content(prompt).text          
                json_string =given_string[given_string.find('{'):given_string.rfind('}') + 1]
                json_objects = json.loads(json_string)
                return json_objects 
            
            except : 
                retry += 1

def generate_coding_questions(Domain_name: str, difficulty_level:str ,num_questions: int = 10): 
        
    prompt = f''' 
    Please generate {num_questions} Coding question ( which can be solve by person in 2 min) the domain of {Domain_name}
    Each question should have hint how to solve it.. 
    and difficulty Level of the coding question Should be : {difficulty_level} 

    Provide the questions and hints in the following JSON format:
    
    outpt should be in this below format :

    Structured output Format : 

    {JSON_FORMATS.get('sort_answers')} 

    The JSON string should be valid and properly formatted to allow for JSON parsing using `json.loads(json_string)`. 
    Only provide the JSON string in the output, without any additional text or explanation '''

    retry  =  0
    while retry < MAX_RETRY : 
            try : 
                given_string = Gemini_Pro.generate_content(prompt).text          
                json_string =given_string[given_string.find('{'):given_string.rfind('}') + 1]
                json_objects = json.loads(json_string)
                return json_objects 
            
            except : 
                retry += 1

def generate_probem_solving_questions(Domain_name: str, difficulty_level:str ,num_questions: int = 10,question_type = 'mcqs'): 
        
    prompt = f''' 
    Please generate {num_questions} Problem Solving Qeustion ( where one Problem is Given As Question and Answerer Need to Solve That ) 
    The domain of {Domain_name}
    Each question should have one Correct answer and hint for that given question  
    and difficulty Level Should be : {difficulty_level} 

    and questions type should be {question_type} generate this given type of teh questions 

    Provide the questions and answers in the following JSON format:
    
    outpt should be in this below format :

    Structured output Format : 

    {JSON_FORMATS.get(question_type)} ''' + '''

    add one more dictionary structure to Above JSON string which is : {'Problem_Description' :'...Detaile Description of Problem Statement...'}  


    The JSON string should be valid and properly formatted to allow for JSON parsing using `json.loads(json_string)`. 
    Only provide the JSON string in the output, without any additional text or explanation '''

    retry  =  0
    while retry < MAX_RETRY : 
            try : 
                given_string = Gemini_Pro.generate_content(prompt).text          
                json_string =given_string[given_string.find('{'):given_string.rfind('}') + 1]
                json_objects = json.loads(json_string)
                return json_objects 
            
            except : 
                retry += 1

def generate_case_study_questions(Domain_name: str, difficulty_level:str ,num_questions: int = 10,question_type = 'mcqs'): 

    prompt = f''' 
    Please generate {num_questions} Questions for Given Case Study (like one case is Provided and Based on that Youl'll need to 
    generate the questions of the domain of {Domain_name}

    and questions type should be {question_type} generate this given type of teh questions 

    and difficulty Level of the coding question Should be : {difficulty_level} 

    Provide the questions and hints in the following JSON format:
    
    outpt should be in this below format :

    Structured output Format : 

    {JSON_FORMATS.get(question_type)} ''' + '''

    add one more dictionary structure to Above JSON string which is : {'Case_Study' :'...Detaile Description of Case Study...'}  

    The JSON string should be valid and properly formatted to allow for JSON parsing using `json.loads(json_string)`. 
    Only provide the JSON string in the output, without any additional text or explanation '''

    retry  =  0
    while retry < MAX_RETRY : 
            try : 
                given_string = Gemini_Pro.generate_content(prompt).text          
                json_string =given_string[given_string.find('{'):given_string.rfind('}') + 1]
                json_objects = json.loads(json_string)
                return json_objects 
            
            except : 
                retry += 1

def generate_senario_based_questions(Domain_name: str, difficulty_level:str ,num_questions: int = 10,question_type = 'mcqs'): 
    
    prompt = f''' 
    Please generate {num_questions} Senario Based Questions ( Scenario-based questions present a -
    hypothetical or real-world situation and ask the respondent to analyze the scenario, make decisions, or solve problems based on the given information) 
    
    generate the questions of the domain of {Domain_name}
    
    and questions type should be {question_type} generate this given type of teh questions 

    and difficulty Level of question Should be : {difficulty_level} 

    Provide the questions and hints in the following JSON format:
    
    outpt should be in this below format :

    Structured output Format : 

    {JSON_FORMATS.get(question_type)} ''' + '''

    add one more dictionary structure to Above JSON string which is : {'Senario_Description' :'...Detaile Description of Senario...'}  

    The JSON string should be valid and properly formatted to allow for JSON parsing using `json.loads(json_string)`. 
    Only provide the JSON string in the output, without any additional text or explanation '''

    retry  =  0
    while retry < MAX_RETRY : 
            try : 
                given_string = Gemini_Pro.generate_content(prompt).text          
                json_string =given_string[given_string.find('{'):given_string.rfind('}') + 1]
                json_objects = json.loads(json_string)
                return json_objects 
            
            except : 
                retry += 1

def evaluate_answer(question: str, answer: str,Domain_name: str = None,answer_type:str= 'short') -> str:
    prompt = f'''
        You are tasked with evaluating a answer provided for a question of given domain ,
        The answer will be rated on a scale of 1 to 10, where 1 is the lowest and 10 is the highest. 
        Your evaluation should be strict, providing lower ratings for incorrect or poor-quality answers, 
        and higher ratings only for accurate and well-explained answers. Additionally, 
        provide detailed feedback that includes guidance, modifications, or changes that could improve the answer.

        Example: 
        Domain Name: Computer Science

        Question: "What does CPU stand for?"
        Provided Answer: "Central Processing Unit" ''' + '''

        Output:
        {
        "feedback": "The answer 'Central Processing Unit' is correct. It accurately identifies what CPU stands for. To further improve, you could mention that the CPU is often referred to as the brain of the computer, responsible for executing instructions from programs.",
        "rating": "10"
        }

        Question: "What does CPU stand for?"
        Provided Answer: "Computer Processing Unit"

        Output:
        {
        "feedback": "The answer 'Computer Processing Unit' is incorrect. CPU stands for 'Central Processing Unit'. It is crucial to use the correct term as it represents the main component of a computer responsible for processing instructions.",
        "rating": "3"
        }

        Question: "What does CPU stand for?"
        Provided Answer: "It is the part of the computer that processes data."

        Output:
        {
        "feedback": "The answer is partially correct but not specific enough. CPU stands for 'Central Processing Unit'. Your description of its function is correct, but it is important to also correctly identify the term.",
        "rating": "5"
        }
        This example is for illustration purposes only. Generate unique content based on the provided data.

        * Output format:
        Ensure the output is in a structured JSON format as follows:
        {
        "feedback": "...",
        "rating": "..."
        }
        
        The JSON string should be valid and properly formatted to allow for JSON parsing using `json.loads(json_string)`. 
        Only provide the JSON string in the output, without any additional text or explanation.''' + f'''
        
        Now  
        The question is : {question} , Domain name is : { Domain_name }
        and answer is : {answer}  
        and this answer is for the {answer_type} type of Question-Answer. 
        so Please Evaluate this based on all given criteria ''' 

    retry  =  0
    while retry < MAX_RETRY : 
            try : 
                given_string = Gemini_Pro.generate_content(prompt).text          
                json_string =given_string[given_string.find('{'):given_string.rfind('}') + 1]
                json_objects = json.loads(json_string)
                return json_objects 
            
            except : 
                retry += 1
                