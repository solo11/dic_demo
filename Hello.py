import streamlit as st

# st.markdown("""
# <style>
# .big-font {
#     width: 1000px;   
#     font-size:40px !important;
# }
# </style>
# """, unsafe_allow_html=True)

st.sidebar.success("Select a page above.")

st.title('Select a demo to view')
st.subheader('1. Predict cancellation based on the booking data, uses model trained on decision tree classifier')
st.subheader('2. View dashboard with visulizations of the booking data')

