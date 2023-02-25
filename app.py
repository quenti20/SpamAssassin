import streamlit as st
import pickle
import cohere
import numpy as np
from cohere.classify import Example

co = cohere.Client('wAjXL30uVWKpRy8vDUiQdC29bjJAv3F1B7s1Uyg3')


examples = pickle.load(open('examples.pkl','rb'))
st.title("Email/SMS Classfier")

def fix_string(s):
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789.,\n')
    s = ''.join(filter(whitelist.__contains__,s))
    return s

input_message = st.text_area("Enter Message")

transform_msg = fix_string(input_message)
transform_msg_list = [transform_msg]

if st.button('Predict'):

    if transform_msg_list:
        response = co.classify(model='small', inputs=transform_msg_list, examples=examples)
        if response:
            result = response[0].prediction
            if result == 'spam': 
                st.header("Spam")
            else: 
                st.header("Not Spam")
    else:
        input_message = "Enter The message please" 


