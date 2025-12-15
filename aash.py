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

# ------------------ APP CONTENT ------------------
st.title("AASH / عادي أي شي")
st.subheader("يحلك المشكلة إذا متوهق وما تدري شنو تاكل")

choices = [
    "Swaikhat",
    "Agnii",
    "Amman Bhelpuri",
    "Ghadeer Al Bahrain",
    "Al Sayed Lebanese Restaurant",
    "Tampopo - Ramen Shop",
    "Meme's Curry",
    "Naranj",
    "Elamigos Restaurant Ras",
    "Midar",
    "Cantina",
    "San Ristorante",
    "Agnii (The Avenues)",
    "Copper Chimney - Indian Restaurant",
    "Matbakhi by Sawsan",
    "Principale Ristorante Di Nino",
    "Assaha Restaurant",
    "The Sandwich Shop",
    "Seoulian",
    "SOLO Pizza Napulitana",
    "Zlatni Juli",
    "Vigonovo",
    "Tekka Lumee",
    "Pinolo Ristorante",
    "Ori Omakase Sushi",
    "BARBA",
    "San Opera",
    "YUKAI",
    "Giulia by Vigonovo",
    "Folio Bistro & Bakery",
    "Wok n roll"
]

# ------------------ BUTTON LOGIC ------------------
if st.session_state.show_button:
    if st.button("اختيار عشوائي", use_container_width=True):
        st.session_state.count += 1

        if st.session_state.count < 4
            st.markdown(
                f"<div class='result-box'>{random.choice(choices)}</div>",
                unsafe_allow_html=True
            )

        if st.session_state.count == 4:
            st.session_state.show_button = False

# ------------------ FINAL MESSAGE ------------------
if st.session_state.count == 4:
    st.success("اشتر اش من الجمعيه ASH")
