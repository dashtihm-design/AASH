import streamlit as st
import random
import re
from restaurant_list import choices

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

# ------------------ APP CONTENT ------------------
st.title("AASH / عادي أي شي")
st.subheader("يحلك المشكلة إذا متوهق وما تدري شنو تاكل")


# ------------------ BUTTON LOGIC ------------------
if st.session_state.show_button:
    if st.button("اختيار عشوائي", use_container_width=True):
        st.session_state.count += 1

        if st.session_state.count < 4:
            text = random.choice(choices)
        
            url = re.search(r'(https?://\S+)', text).group(1)
            name = text.replace(url, '').strip()
        
            st.markdown(
                f"""
                <div class='result-box'>
                    <a href="{url}" target="_blank">{name}</a>
                </div>
                """,
                unsafe_allow_html=True
            )

        if st.session_state.count == 4:
            st.session_state.show_button = False

# ------------------ FINAL MESSAGE ------------------
if st.session_state.count == 4:
    st.success("اشتر اش من الجمعيه ASH")
