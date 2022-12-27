import streamlit as st
import pickle
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

# Function for processing the input message/sms
def process_msg(message):
    msg = re.sub('[^a-zA-Z]', ' ', message)
    msg = msg.lower()
    msg = nltk.word_tokenize(msg)
    y = []
    for i in msg:
        if i.isalnum():
            y.append(i)
    msg = y[:]
    y.clear()
    for i in msg:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    msg = y[:]
    y.clear()
    for i in msg:
        y.append(ps.stem(i))
    return ' '.join(y)

# Load in model and vectorizer
tfidf = pickle.load(open('../SMS_spam_detection/Models/vectorizer.pkl', 'rb'))
model = pickle.load(open('../SMS_spam_detection/Models/model.pkl', 'rb'))

# Getting input message
st.title('SMS Spam Detector')
input_msg = st.text_input('Enter the message to be classified')

# Button for predicting input message
if st.button('Predict'):
    # Processing the message
    processed_msg = process_msg(input_msg)
    vector_input = tfidf.transform([processed_msg])
    result = model.predict(vector_input)[0]

    # Displaying prediction result 
    if result == 1:
        st.header('Spam')
    else:
        st.header('Ham')