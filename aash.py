import streamlit as st
import random

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AASH",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ------------------ SESSION STATE ------------------
if "count" not in st.session_state:
    st.session_state.count = 0

if "show_button" not in st.session_state:
    st.session_state.show_button = True

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# ------------------ DARK MODE TOGGLE ------------------
st.toggle("Dark Mode", key="dark_mode")

# ------------------ THEMES ------------------
if st.session_state.dark_mode:
    bg_color = "#0E1117"
    text_color = "#FAFAFA"
    card_color = "#1E2228"
    button_color = "#262730"
else:
    bg_color = "#FFFFFF"
    text_color = "#000000"
    card_color = "#F1F3F6"
    button_color = "#E0E0E0"

# ------------------ CUSTOM CSS ------------------
st.markdown(f"""
<style>
    body {{
        background-color: {bg_color};
        color: {text_color};
        direction: rtl;
        text-align: center;
    }}

    .stApp {{
        background-color: {bg_color};
    }}

    .stButton > button {{
        height: 60px;
        font-size: 20px;
        border-radius: 15px;
        background-color: {button_color};
        color: {text_color};
        border: none;
    }}

    .result-box {{
        background-color: {card_color};
        padding: 20px;
        border-radius: 15px;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }}
</style>
""", unsafe_allow_html=True)

# ------------------ APP CONTENT ------------------
st.title("AASH / عادي أي شي")
st.subheader("يحلك المشكلة إذا متوهق وما تدري شنو تاكل")

choices = [
    "Solo Napultina",
    "Barba",
    "Elevation",
    "Pick"
]

# ------------------ BUTTON LOGIC ------------------
if st.session_state.show_button:
    if st.button("اختيار عشوائي", use_container_width=True):
        st.session_state.count += 1

        if st.session_state.count < 4:
            st.markdown(
                f"<div class='result-box'>{random.choice(choices)}</div>",
                unsafe_allow_html=True
            )

        if st.session_state.count >= 3:
            st.session_state.show_button = False

# ------------------ FINAL MESSAGE ------------------
if st.session_state.count >= 3:
    st.success("ASH")
