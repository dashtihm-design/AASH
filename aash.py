import streamlit as st
import random
from restaurant_list import choices

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AASH",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ------------------ CSS FOR SQUARE MAP ------------------
st.markdown(
    """
    <style>
    .square-map {
        position: relative;
        width: 100%;
        padding-bottom: 100%; /* 1:1 aspect ratio */
        height: 0;
        overflow: hidden;
        border-radius: 12px;
    }
    .square-map iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ SESSION STATE ------------------
if "count" not in st.session_state:
    st.session_state.count = 0

if "show_button" not in st.session_state:
    st.session_state.show_button = True
