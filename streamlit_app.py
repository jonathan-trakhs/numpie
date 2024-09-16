import streamlit as st
import numpie as npie

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write(
    "NP Version: " + npie.activeVersion()
)