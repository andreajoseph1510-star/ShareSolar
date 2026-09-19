
# ShareSolar 🌞

## Overview

**ShareSolar** is a community-driven platform that enables households to **share rooftop solar energy**, distribute excess energy fairly, and reduce dependence on conventional energy sources.

Built during a hackathon, ShareSolar demonstrates how data, backend services, and voice-enabled features can support more accessible and sustainable community energy sharing.

---

## 🚀 Live Demo

🔗 **[Try ShareSolar Live](https://sharesolar.streamlit.app/)**

> The live demo is deployed using Streamlit Community Cloud.

---

## 🎥 Demo

A complete demonstration of ShareSolar is available here:

🔗 **[Watch the Demo Video](https://drive.google.com/file/d/1gxD-4IgFRqMnAQJyF94WgotE-DT69QQG/view?usp=sharing)**

---

## Problem

Many households generate solar power but cannot fully utilize their excess energy.

- ☀️ Solar-producing households may have unused excess energy.
- 🏠 Nearby households may have additional energy requirements.
- 🤝 There is a need for fair and transparent community energy sharing.
- 🌍 Greater use of renewable energy can contribute to reduced dependence on fossil fuels.

---

## 💡 Solution

ShareSolar provides a platform for understanding and managing community-level solar energy sharing.

The application includes:

- 📊 Household solar generation and usage data
- ⚡ Excess-energy calculation
- 🤝 Community energy-sharing insights
- 📈 Household energy comparison
- 🎙️ Text-to-Speech functionality
- 🗣️ Speech-to-Text functionality
- 🔊 Voice-based community summaries
- 🖥️ FastAPI backend for processing and APIs

---

## ✨ Key Features

### 📊 Household Dashboard

Displays household-level:

- Solar generation
- Energy usage
- Excess/deficit energy
- Comparative visualizations

### 🤝 Community Summary

Provides an overview of energy generation, consumption, and available excess energy across the community.

### 🎙️ Voice Features

ShareSolar includes accessibility-focused voice functionality:

- **Text-to-Speech** – converts written information into speech.
- **Speech-to-Text** – converts uploaded audio into text.
- **Community Voice Summary** – provides an audio summary of community energy information.

---

## 📸 Screenshots

### 🏠 Household Dashboard

![Household Dashboard](<img width="1917" height="842" alt="Screenshot 2026-09-19 110654" src="https://github.com/user-attachments/assets/286409c3-8204-4bd3-aefe-a25652b0f86d" />
)
![Bar graph](<img width="1852" height="702" alt="Screenshot 2026-09-19 110709" src="https://github.com/user-attachments/assets/2ed52b41-7a3d-44b6-a85c-0119911c868e" />)
![Pie chart](<img width="1818" height="847" alt="Screenshot 2026-09-19 110718" src="https://github.com/user-attachments/assets/59eb9231-0eef-4c25-9f03-c06249998409" />)



### 🤝 Community Summary

![Community Summary](<img width="1897" height="735" alt="Screenshot 2026-09-19 110727" src="https://github.com/user-attachments/assets/f5cc9caa-8a7e-4f09-b17e-a177da533e24" />
)

### 🎙️ Voice Features

![Voice Features](<img width="1800" height="731" alt="Screenshot 2026-09-19 110745" src="https://github.com/user-attachments/assets/428e1e0e-6add-4f2f-acda-ec21ca5bb1d8" />
)

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend / Dashboard | Streamlit |
| Backend | FastAPI |
| Programming Language | Python |
| Speech-to-Text | Whisper |
| Text-to-Speech | gTTS |
| Data Processing | Pandas |
| Deployment | Streamlit Community Cloud |

---

## 📈 Impact

ShareSolar aims to support:

- 🌍 Reduced dependence on fossil-fuel-based electricity
- ☀️ Better utilization of rooftop solar generation
- 🤝 Community-based energy sharing
- 💡 Greater awareness of household energy usage
- ♻️ More efficient use of renewable energy

---

## 🔮 Future Enhancements

The current prototype can be extended with:

- 🔋 **Real-time IoT integration** for live solar generation and consumption data
- ⚡ **Automated energy matching** between households with surplus and energy demand
- 💰 **Dynamic pricing and fair settlement** for shared energy
- 🗺️ **Community energy map** showing participating households
- 🔐 **Secure user authentication and household profiles**
- 📱 **Mobile application** for easier community access
- 🤖 **AI-powered energy recommendations** for households
- 📊 **Predictive energy forecasting** using historical generation and consumption data
- 🌐 **Integration with smart meters** for real-world deployment
- 🗣️ **Multilingual voice support** for improved accessibility

---

## 🏗️ Project Architecture

```text
User
 │
 ▼
Streamlit Dashboard
 │
 ├── Household Data
 ├── Community Summary
 └── Voice Features
       │
       ├── Text-to-Speech
       └── Speech-to-Text
 │
 ▼
FastAPI Backend
 │
 ▼
Data Processing & Energy Sharing Logic
