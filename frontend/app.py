import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="ShareSolar Dashboard", layout="wide")

# Custom CSS for yellow headings
st.markdown("""
<style>

.sun {
    position: absolute;
    top: 35px;
    left: 30px;
    font-size: 100px;
    z-index: 999999;
    animation: sunGlow 1.8s ease-in-out infinite;
}

@keyframes sunGlow {
    0%, 100% {
        transform: scale(1);
        filter: drop-shadow(0 0 5px #FFD700);
    }

    50% {
        transform: scale(1.12);
        filter: drop-shadow(0 0 20px #FF9800)
                drop-shadow(0 0 35px #FFD700);
    }
}

</style>

<div class="sun">☀️</div>
""", unsafe_allow_html=True)



st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #FFF3B0, #FFD166, #FFB347);
}
/* Main title */
.share-title {
    text-align: center;
    font-size: 50px;
    font-weight: 700;
    color: #8B4513;
    margin-bottom: 25px;
}
/* Section headings */
.section-yellow {
    color: #7A3E00 !important;
    font-weight: 700 !important;
}

/* Center the tabs */
[data-baseweb="tab-list"] {
    justify-content: center !important;
    gap: 10px;
}

/* Tab text - BLUE */
button[data-baseweb="tab"] {
    color: #1976D2 !important;
}

/* Active tab - darker blue */
button[data-baseweb="tab"][aria-selected="true"] {
    color: #1565C0 !important;
}

/* Active tab underline */
button[data-baseweb="tab"][aria-selected="true"]::after {
    background-color: #1976D2 !important;
}
</style>
""", unsafe_allow_html=True)


# Title
st.markdown(
    '<div class="share-title">ShareSolar Dashboard</div>',
    unsafe_allow_html=True
)
st.markdown("""
<style>
button[data-baseweb="tab"] {
    justify-content: center;
}

[data-baseweb="tab-list"] {
    justify-content: center;
}
</style>

""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Voice Features headings and text */
h1, h2, h3, p, label {
    color:#7A3E00 !important;
}

/* Text input placeholder */
.stTextInput input,
.stTextArea textarea {
    color: #C49A6C !important;
}

/* Uploaded file information */
[data-testid="stFileUploader"] {
    color: #7A3E00 !important;
}

</style>
""", unsafe_allow_html=True)
# Tabs for navigation
tab1, tab2, tab3 = st.tabs([" Household Data", " Community Summary", "🎤 Voice Features"])

# --- Household Data Tab ---
with tab1:
    st.markdown('<p class="section-yellow">Household Data 🏠</p>', unsafe_allow_html=True)
    try:
        data = requests.get("https://sharesolar.onrender.com/households").json()
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

        # Bar chart
        st.subheader("Household Energy Comparison")
        st.bar_chart(df.set_index("household")[["generation", "usage", "excess"]])

        # Side-by-side pie charts
        st.subheader("Use vs Generation Pie Charts")

        fig, ax = plt.subplots(1, 2, figsize=(10, 5))

        df.set_index("household")["generation"].plot.pie(
            ax=ax[0],
            autopct='%1.1f%%',
            startangle=90,
            legend=False,
            radius=0.8
        )

        ax[0].set_ylabel("")
        ax[0].set_title("Generation")

        df.set_index("household")["usage"].plot.pie(
            ax=ax[1],
            autopct='%1.1f%%',
            startangle=90,
            legend=False,
            radius=0.7
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
        summary = requests.get("https://sharesolar.onrender.com/summary").json()

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
   
    st.title("Voice Features 🎙️")

    # --- Text to Speech ---
    st.subheader("Text to Speech")
    text_input = st.text_input("Enter text to speak")
    if st.button("Speak"):
        response = requests.post("https://sharesolar.onrender.com/voice/speak", params={"text": text_input})
        with open("spoken.mp3", "wb") as f:
            f.write(response.content)
        st.audio("spoken.mp3")

    # --- Speech to Text ---
    st.subheader("Speech to Text")
    uploaded_file = st.file_uploader("Upload audio file", type=["mp3", "wav"])
    if uploaded_file and st.button("Upload"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("https://sharesolar.onrender.com/voice/transcribe", files=files)
        st.write(response.json())

    # --- Speak Community Summary ---
    st.subheader("Community Voice Summary")
    if st.button("Speak Community Summary"):
        response = requests.get("https://sharesolar.onrender.com/voice/summary")
        with open("summary.mp3", "wb") as f:
            f.write(response.content)
        st.audio("summary.mp3")
