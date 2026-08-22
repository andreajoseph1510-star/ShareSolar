import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="ShareSolar Dashboard", layout="wide")

# Custom CSS for yellow headings
st.markdown(
    """
    <style>
    .big-yellow {
        color: yellow;
        font-size: 32px;
        font-weight: bold;
    }
    .section-yellow {
        color: yellow;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<p class="big-yellow">🌞 ShareSolar Dashboard</p>', unsafe_allow_html=True)

# Tabs for navigation
tab1, tab2, tab3 = st.tabs(["🏠 Household Data", "⚡ Community Summary", "🎤 Voice Features"])

# --- Household Data Tab ---
with tab1:
    st.markdown('<p class="section-yellow">Household Data 🏠</p>', unsafe_allow_html=True)
    try:
        data = requests.get("http://127.0.0.1:8000/households").json()
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

        # Bar chart
        st.subheader("Household Energy Comparison")
        st.bar_chart(df.set_index("household")[["generation", "usage", "excess"]])

        # Side-by-side pie charts
        st.subheader("Usage vs Generation Pie Charts")
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))

        df.set_index("household")["generation"].plot.pie(
            ax=ax[0], autopct='%1.1f%%', startangle=90, legend=False
        )
        ax[0].set_ylabel("")
        ax[0].set_title("Generation")

        df.set_index("household")["usage"].plot.pie(
            ax=ax[1], autopct='%1.1f%%', startangle=90, legend=False
        )
        ax[1].set_ylabel("")
        ax[1].set_title("Usage")

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error loading households: {e}")

# --- Community Summary Tab ---
with tab2:
    st.markdown('<p class="section-yellow">Community Summary ⚡</p>', unsafe_allow_html=True)
    try:
        summary = requests.get("http://127.0.0.1:8000/summary").json()

        # Metrics side by side
        col1, col2, col3 = st.columns(3)
        col1.metric("🌞 Total Generation", f"{summary['total_generation']} kWh")
        col2.metric("⚡ Total Usage", f"{summary['total_usage']} kWh")
        col3.metric("➕ Total Excess", f"{summary['total_excess']} kWh")

        # Progress bar for usage percentage
        usage_pct = round(summary['total_usage'] / summary['total_generation'] * 100, 1)
        st.progress(int(usage_pct))
        st.write(f"Community used {usage_pct}% of generated energy.")

    except Exception as e:
        st.error(f"Error loading summary: {e}")

# --- Voice Features Tab ---
with tab3:
    st.markdown('<p class="section-yellow">Voice Features 🎤</p>', unsafe_allow_html=True)

    # Text to Speech
    st.subheader("Text to Speech")
    text = st.text_input("Enter text to speak")
    if st.button("Speak"):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/voice/speak",
                params={"text": text, "language": "en"}
            )
            with open("output.mp3", "wb") as f:
                f.write(response.content)
            st.audio("output.mp3")
        except Exception as e:
            st.error(f"Error generating speech: {e}")

    # Speech to Text
    st.subheader("Speech to Text")
    uploaded_file = st.file_uploader("Upload audio file", type=["mp3", "wav"])
    if uploaded_file and st.button("Transcribe"):
        try:
            files = {"file": uploaded_file.getvalue()}
            response = requests.post("http://127.0.0.1:8000/voice/transcribe", files=files)
            st.write("Transcript:", response.json()["transcript"])
        except Exception as e:
            st.error(f"Error transcribing audio: {e}")
