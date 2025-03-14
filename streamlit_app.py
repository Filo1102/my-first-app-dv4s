import streamlit as st

st.title("My new Streamlit app")
st.write(
    "Welcome to my new app!"
)

data = st.slider("Select a value", 0, 100, 50)
st.write("You selected:", data)