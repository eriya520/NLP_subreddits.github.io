#imports
import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(
    page_icon='🌿',
    initial_sidebar_state='expanded'
)

st.title("""
Subreddits sentiments on brand wars: Whole Foods or Trader Joes?
""")

st.write("Trader Joe's and Wholefoods are two popular grocery chains who boast organic and sustainable products. Trader Joe’s owned by ALDI, and Whole Foods are brought by Amazon in 2017.")
img=Image.open('brands.jpg')
st.image(img)
st.write('''They are often considered as competitors, but they are very different animals in terms of:
* Store size
* Product mix
* Private labels 
* Sourcing
* ...
''')

st.write("""
**However, they have 95% overall in customers that shop both stores.**\n
Most of the customers would shop at both stores looking for organic, healthy produces.
""")

st.markdown("<h4> We will look at the sentiments from subreddits submitted posts on the two organic stores. Time for the show-down!</h4>", unsafe_allow_html=True)
selection = st.sidebar.selectbox("Make a selection",("Sentiment score","Prediction on posts"))

if selection == 'Sentiment score':
    st.subheader('Sentiment Analysis on subreddit posts')
    st.title('SentimentAnalysis is used for positive and negative scores on subreddit posts')

elif selection =='Prediction on posts':
    st.subheader('Make a prediction on the posts to decide which subreddits it belongs to')
    st.title('Classification model is able to predict the posts belongs to store as follow:')