import streamlit as st
import random
from collections import Counter

# จำลองข้อมูลการค้นหาของผู้ใช้จาก Google
def simulate_google_search_history(user_id):
    search_histories = {
        1: ["แอคชั่นมันๆ", "หนังผจญภัย", "หนังซูเปอร์ฮีโร่", "รีวิวหนังแอคชั่น"],
        2: ["ตลกฮาๆ", "หนังรักโรแมนติก", "คอมเมดี้ยอดนิยม", "หนังตลกครอบครัว"],
        3: ["หนังดราม่าซึ้งๆ", "หนังชีวประวัติ", "หนังรางวัลออสการ์", "ดราม่าน้ำตาซึม"],
        4: ["หนังไซไฟสุดล้ำ", "นิยายวิทยาศาสตร์", "หนังเอเลี่ยน", "หนังอวกาศ"]
    }
    return search_histories.get(user_id, [])

# วิเคราะห์ความชอบของผู้ใช้
def analyze_user_preference(search_history):
    keywords = {
        "แอคชั่น": ["แอคชั่น", "ผจญภัย", "ซูเปอร์ฮีโร่"],
        "ตลก": ["ตลก", "คอมเมดี้", "ฮา"],
        "ดราม่า": ["ดราม่า", "ชีวประวัติ", "ซึ้ง", "รางวัล"],
        "ไซไฟ": ["ไซไฟ", "วิทยาศาสตร์", "เอเลี่ยน", "อวกาศ"]
    }
    
    preference_count = Counter()
    for search in search_history:
        for genre, words in keywords.items():
            if any(word in search.lower() for word in words):
                preference_count[genre] += 1
    
    if preference_count:
        return preference_count.most_common(1)[0][0]
    return "ไม่ระบุ"

# ข้อมูลหนังตัวอย่าง
movies = {
    "แอคชั่น": ["The Dark Knight - แบทแมน อัศวินรัตติกาล", "Inception - จิตพิฆาตโลก", "Mad Max: Fury Road - แมด แม็กซ์: ถนนโลกันตร์"],
    "ตลก": ["The Hangover - เมายกแก๊ง แฮงค์ยกก๊วน", "Bridesmaids - เพื่อนเจ้าสาว แสบรั่วตัวแม่", "Superbad - ซูเปอร์แบด วันพลาดโดนเต็ม"],
    "ดราม่า": ["The Shawshank Redemption - ชอว์แชงค์ มิตรภาพ ความหวัง ความรุนแรง", "Forrest Gump - ฟอร์เรสท์ กัมพ์", "The Godfather - เดอะ ก็อดฟาเธอร์"],
    "ไซไฟ": ["Interstellar - อินเตอร์สเตลลาร์ ทะยานดาวกู้โลก", "The Matrix - เดอะ เมทริกซ์", "Blade Runner - เบลด รันเนอร์"]
}

def get_recommendation(genre):
    return random.choice(movies.get(genre, random.choice(list(movies.values()))))

def main():
    st.title("แชทบอทแนะนำหนังอัจฉริยะ")

    # สร้าง session state สำหรับ user_id ถ้ายังไม่มี
    if 'user_id' not in st.session_state:
        st.session_state.user_id = random.randint(1, 4)

    # ดึงและวิเคราะห์ข้อมูลการค้นหา
    search_history = simulate_google_search_history(st.session_state.user_id)
    preferred_genre = analyze_user_preference(search_history)

    st.write(f"ยินดีต้อนรับ ผู้ใช้หมายเลข {st.session_state.user_id}!")
    st.write(f"จากการวิเคราะห์ประวัติการค้นหาของคุณ เราพบว่าคุณชอบหนังแนว {preferred_genre}")

    if st.button("แนะนำหนังตามความชอบของฉัน"):
        recommendation = get_recommendation(preferred_genre)
        st.write(f"เราขอแนะนำหนังเรื่อง: {recommendation}")

    # ให้ผู้ใช้เลือกแนวหนังเองได้ด้วย
    user_genre = st.selectbox(
        "หรือคุณอยากเลือกแนวหนังเองไหม?",
        ["เลือกแนวหนัง"] + list(movies.keys())
    )

    if user_genre != "เลือกแนวหนัง":
        if st.button("แนะนำหนังตามที่ฉันเลือก"):
            recommendation = get_recommendation(user_genre)
            st.write(f"สำหรับหนังแนว{user_genre} เราขอแนะนำเรื่อง: {recommendation}")

if __name__ == "__main__":
    main()