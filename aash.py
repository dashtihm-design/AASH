import streamlit as st
import random
import re

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
    "Swaikhat  https://maps.app.goo.gl/EjE9bMXvsfpjJGdh7",
    "Amman Bhelpuri  https://maps.app.goo.gl/4N9vGAfdzQwpfbLcA",
    "Ghadeer Al Bahrain  https://maps.app.goo.gl/naAnZuPffcDbJFNcA",
    "Al Sayed Lebanese Restaurant  https://maps.app.goo.gl/QXFPHig1t5g1WKkL9",
    "Tampopo - Ramen Shop  https://maps.app.goo.gl/Y8wEdPwAt54cw2Ns6",
    "Meme's Curry  https://maps.app.goo.gl/bJrfdVByaQHjoKQR9",
    "Naranj  https://maps.app.goo.gl/eopzWbfrm43XYiYT6",
    "Elamigos Restaurant Ras  https://maps.app.goo.gl/cXHTsttqNP28YS1BA",
    "Midar  https://maps.app.goo.gl/gghCfL6tYemQ8pmE8",
    "Cantina  https://maps.app.goo.gl/Qqd3ZUwi91YVPEkc8",
    "San Ristorante  https://maps.app.goo.gl/C6qtozPRTRrbK1Mv7",
    "Agnii (The Avenues)  https://maps.app.goo.gl/3XN9fQtzgX6tw6kK9",
    "Copper Chimney - Indian Restaurant  https://maps.app.goo.gl/7e9Ra34a77Uybjep6",
    "Matbakhi by Sawsan  https://maps.app.goo.gl/ZfbJceGMzsic2PBP9",
    "Principale Ristorante Di Nino  https://maps.app.goo.gl/PnEEHf3amn3CzKhM9",
    "Assaha Restaurant  https://maps.app.goo.gl/jA1ACZqeAETPxoGo8",
    "The Sandwich Shop https://maps.app.goo.gl/2xarP2AiJdGYj5HZ6",
    "Seoulian  https://maps.app.goo.gl/67ny89t2t7LyxwDLA",
    "SOLO Pizza Napulitana https://maps.app.goo.gl/zXWYVk3ZWmshtUwZ6",
    "Zlatni Juli  https://maps.app.goo.gl/iQU8uiWr3KjTuQhVA",
    "Vigonovo https://maps.app.goo.gl/fY4vrJVqJzHZFTCo8",
    "Tekka Lumee  https://maps.app.goo.gl/21TdcUzF254amC518",
    "Pinolo Ristorante  https://maps.app.goo.gl/P8Hnu1ZLMgcBtdCi8",
    "Ori Omakase Sushi  https://maps.app.goo.gl/KeVJ7aAvezaJyB5TA",
    "BARBA  https://maps.app.goo.gl/YPsUY4tyevBsBjpA8",
    "San Opera  https://maps.app.goo.gl/5RG7jQ4gr1pBkKEx5",
    "YUKAI  https://maps.app.goo.gl/KHmomeH6hVzbjXY59",
    "Giulia by Vigonovo  https://maps.app.goo.gl/aPxjqc7ggnX2LPSU9",
    "Folio Bistro & Bakery  https://maps.app.goo.gl/kTinT9YhG5RDnUnC8",
    "Wok n roll  https://maps.app.goo.gl/pK2higCjHUxskyoe6"
]

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
