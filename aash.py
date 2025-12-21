import streamlit as st
import random
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
            choice = random.choice(choices)

            if not isinstance(choice, dict):
                st.error("restaurant_list.py is not updated correctly")
                st.stop()

            with st.container(border=True):
                st.markdown(f"## 🍽️ {choice['name']}")
                st.markdown(f"[📍 فتح الموقع في Google Maps]({choice['map_url']})")

                # ---- GOOGLE MAPS EMBED (includes real photos) ----
                st.components.v1.iframe(
                    choice["embed_url"],
                    height=350,
                    scrolling=False
                )

        if st.session_state.count == 4:
            st.session_state.show_button = False

# ------------------ FINAL MESSAGE ------------------
if st.session_state.count == 4:
    st.success("اشتر اش من الجمعيه ASH")
