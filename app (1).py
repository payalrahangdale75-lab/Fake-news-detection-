import streamlit as st
import pickle
import sqlite3
from datetime import datetime

# ---------- Database (SQLite) ----------
@st.cache_resource
def get_conn():
    conn = sqlite3.connect("predictions.db", check_same_thread=False)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            news TEXT,
            result TEXT,
            created_at TEXT
        )"""
    )
    conn.commit()
    return conn

conn = get_conn()

# ---------- Load Model ----------
@st.cache_resource
def load_model():
    with open("fake_news_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# ---------- UI ----------
st.title("📰 Fake News Detection")

st.write("Enter a news article and click Predict.")

st.caption("🤖 Model: Passive Aggressive Classifier + TF-IDF")

st.info("💡 For best results, paste a complete news article instead of a single sentence or headline.")

st.warning("""
⚠️ Disclaimer

• This model is trained on a historical dataset.
• Predictions are based only on the input text and are not 100% accurate.
• The model may not recognize recent events or newly emerging news.
• Please verify important news from trusted sources before making any decisions.

This project is developed for educational and demonstration purposes.
""")

st.markdown("---")

news = st.text_area("Enter News", height=200)

if st.button("Predict"):
    if news.strip() == "":
        st.warning("⚠ Please enter a news article.")
    else:
        prediction = model.predict([news])
        label = "Fake" if prediction[0] == 0 else "True"

        # Save to database
        conn.execute(
            "INSERT INTO predictions (news, result, created_at) VALUES (?, ?, ?)",
            (news, label, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        conn.commit()

        if label == "Fake":
            st.error("🚨 Fake News")
        else:
            st.success("✅ True News")

# ---------- History from database ----------
st.markdown("---")
st.subheader("🗂 Prediction History")

total = conn.execute("SELECT COUNT(*) FROM predictions").fetchone()[0]
fake = conn.execute("SELECT COUNT(*) FROM predictions WHERE result='Fake'").fetchone()[0]
st.write(f"Total: **{total}** | Fake: **{fake}** | True: **{total - fake}**")

rows = conn.execute(
    "SELECT created_at, result, news FROM predictions ORDER BY id DESC LIMIT 10"
).fetchall()

if rows:
    st.table(
        [
            {
                "Time": t,
                "Result": r,
                "News": (n[:80] + "...") if len(n) > 80 else n,
            }
            for t, r, n in rows
        ]
    )
else:
    st.caption("No predictions yet.")

st.caption("ℹ️ Entered text and results are saved in a database for history.")

st.markdown("---")
st.markdown("**Developed By:** Payal Rahangdale")
