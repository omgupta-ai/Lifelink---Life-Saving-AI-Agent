# 🪼 Lifelink: A Life-Saving AI Agent

**Lifelink** is a sophisticated, agentic AI system designed to provide empathetic mental health support and immediate crisis intervention. By combining the reasoning power of **Llama 3** (via Groq) with the clinical depth of **MedGemma** (via Ollama), Lifelink bridges the gap between conversational AI and real-world safety protocols.

---

## ✨ Key Features

* **🧠 Hybrid Intelligence Architecture**: Uses a multi-model approach. **Llama 3** acts as the Agent Orchestrator while **MedGemma:4b** provides specialized clinical responses.
* **🛠️ Full-Suite Tool Integration**:
    * **`ask_mental_health_specialist`**: Deep therapeutic conversations using MedGemma.
    * **`find_nearby_therapists_by_location`**: Automatically detects user location or queries specific areas to find licensed professional help nearby.
    * **`emergency_call_tool`**: High-priority safety tool using **Twilio Voice API**.
* **🚨 Multi-Tier Emergency Response**:
    * Detects suicidal ideation or crisis intent in real-time.
    * Automatically places calls to **911 (Emergency Services)**.
    * Simultaneously alerts a **Personal Emergency Contact** defined in the system.
* **⚡ Groq-Powered Speed**: Near-instantaneous response times using Groq's LPU™ technology, ensuring no delays during critical moments.

---

## 🏗️ System Architecture

Lifelink is built on a modern, decoupled stack:

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Responsive, chat-based UI for users. |
| **Backend API** | FastAPI | High-performance async gateway for the agent. |
| **Orchestration** | LangGraph | Manages the state and logic of tool-calling loops. |
| **Agent Model** | Llama-3 (Groq) | Orchestrator responsible for reasoning and tool selection. |
| **Clinical Model** | MedGemma (Ollama) | Local clinical model for empathic therapy. |
| **Communications** | Twilio API | Triggers real-world phone calls for safety. |


## 📂 Project Structure

 ```Plaintext
Lifelink/
├── backend/
│   ├── ai_agent.py    # LangGraph orchestration & Tool logic
│   ├── main.py        # FastAPI async endpoints
│   ├── tools.py       # MedGemma, Twilio Call logic, & Geolocation
│   └── config.py      # (Private) API Keys & Secrets
├── frontend.py        # Streamlit Chat Interface
├── .gitignore         # Prevents leaking config.py
└── pyproject.toml     # Dependency management
 ```

---

### Prerequisites
* Python 3.11+
* [Ollama](https://ollama.com/) running locally with `alibayram/medgemma:4b`.
* [Groq API Key](https://console.groq.com/) for orchestration.
* [Twilio Account](https://www.twilio.com/) for voice calls.


