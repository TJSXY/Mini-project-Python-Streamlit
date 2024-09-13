import streamlit as st
import random

# ข้อมูลหนังตัวอย่าง
movies = {
    "แอคชั่น": ["The Dark Knight - แบทแมน อัศวินรัตติกาล", "Inception - จิตพิฆาตโลก", "Mad Max: Fury Road - แมด แม็กซ์: ถนนโลกันตร์"],
    "ตลก": ["The Hangover - เมายกแก๊ง แฮงค์ยกก๊วน", "Bridesmaids - เพื่อนเจ้าสาว แสบรั่วตัวแม่", "Superbad - ซูเปอร์แบด วันพลาดโดนเต็ม"],
    "ดราม่า": ["The Shawshank Redemption - ชอว์แชงค์ มิตรภาพ ความหวัง ความรุนแรง", "Forrest Gump - ฟอร์เรสท์ กัมพ์", "The Godfather - เดอะ ก็อดฟาเธอร์"],
    "ไซไฟ": ["Interstellar - อินเตอร์สเตลลาร์ ทะยานดาวกู้โลก", "The Matrix - เดอะ เมทริกซ์", "Blade Runner - เบลด รันเนอร์"]
}

def get_recommendation(genre):
    return random.choice(movies[genre])

def main():
    st.title("แชทบอทแนะนำหนัง")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # เพิ่มตัวเลือกประเภทหนัง
    genre = st.selectbox(
        "คุณสนใจหนังแนวไหนครับ?",
        ("เลือกประเภทหนัง", "แอคชั่น", "ตลก", "ดราม่า", "ไซไฟ")
    )

    if genre != "เลือกประเภทหนัง":
        if st.button("แนะนำหนัง"):
            recommendation = get_recommendation(genre)
            response = f"สำหรับหนังแนว{genre} ผมขอแนะนำเรื่อง: {recommendation} ครับ"
            
            # Display user request
            st.chat_message("user").markdown(f"ขอคำแนะนำสำหรับหนังแนว{genre}")
            st.session_state.messages.append({"role": "user", "content": f"ขอคำแนะนำสำหรับหนังแนว{genre}"})
            
            # Display bot response
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

    # ช่องสำหรับพิมพ์ข้อความ
    user_input = st.text_input("หรือคุณอยากถามอะไรเพิ่มเติมไหม?")
    if user_input:
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Bot response (simple for now)
        bot_response = "ขอบคุณสำหรับคำถามครับ ผมยังตอบคำถามเพิ่มเติมไม่ได้ แต่ผมสามารถแนะนำหนังให้คุณได้โดยการเลือกประเภทหนังด้านบนครับ"
        with st.chat_message("assistant"):
            st.markdown(bot_response)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

if __name__ == "__main__":
    main()