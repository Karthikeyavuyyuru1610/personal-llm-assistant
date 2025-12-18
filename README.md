# personal-llm-assistant
A personalized, identity-bound AI assistant built with Groq and LLaMA-3 that acts as a Digital Second Brain, using resume data, personality, and short-term memory to deliver human-like responses.
# 🧠 Digital Second Brain
### Identity-Bound Personal AI Assistant using Groq & LLaMA-3

A personalized, identity-bound AI assistant designed to function as a **Digital Second Brain**.  
Unlike generic chatbots, this system is tightly coupled to a single user and responds using their **resume, skills, experience, goals, and personality**.

This project demonstrates **real-world prompt engineering**, **behavior control**, and **personal AI design** using Groq’s ultra-fast LLM inference.

---

## 🚀 Project Overview

The Digital Second Brain is a terminal-based AI assistant that:
- Belongs to **one specific user**
- Understands professional background and career goals
- Responds like a **human assistant**, not a generic bot
- Maintains short-term conversational memory
- Uses **zero fine-tuning** — only structured prompts

Built with:
- **Groq API**
- **LLaMA-3.1-8B-Instant**
- **Python**

---

## 🎯 Key Features

- **Identity-Bound Intelligence**  
  The assistant is explicitly bound to one individual and can accurately describe them when asked.

- **Resume-Aware Responses**  
  Skills, projects, education, and experience are embedded directly into the system prompt.

- **Behavior & Personality Control**  
  Tone, metaphors, conversational style, and engagement rules are enforced via prompt design.

- **Short-Term Memory**  
  Retains recent conversation context for continuity.

- **High-Speed Inference**  
  Powered by Groq for extremely low-latency responses.

---

## 🏗️ System Architecture

User Input  
↓  
System Prompt  
(Identity + Resume + Personality + Rules)  
↓  
Short-Term Chat Memory (Last 6 turns)  
↓  
Groq LLM (LLaMA-3.1-8B-Instant)  
↓  
Personalized AI Response  

No databases  
No vector stores  
No fine-tuning  

Only **clean logic and disciplined prompt engineering**.

---

## 📂 Code Design (High-Level)

### 1. API Configuration
- Loads Groq API securely from environment variables
- Stops execution if the key is missing

Purpose: Safe and explicit LLM access control.

---

### 2. User Profile Injection
- Structured resume data:
  - Education
  - Skills
  - Experience
  - Projects
  - Career goals

Purpose: Permanent user knowledge for the AI.

---

### 3. Personality & Behavioral Layer
- Injects interests, communication style, and engagement patterns
- Prevents robotic responses

Purpose: Human-like interaction.

---

### 4. Chat Memory
- Stores last 6 conversation turns
- Prevents token explosion

Purpose: Short-term contextual awareness.

---

### 5. Core LLM Function
- Constructs the system prompt
- Injects identity, memory, and rules
- Queries Groq LLM
- Returns personalized responses

Purpose: Converts static data into live intelligence.

---

### 6. Terminal Chat Interface
- Interactive CLI loop
- Type `exit` to quit

Purpose: Lightweight, fast experimentation.

---

## ▶️ How to Run

### Step 1: Install Dependency
pip install groq


### Step 2: Set API Key
Linux / macOS:


export GROQ_API_KEY="your_api_key_here"


Windows (PowerShell):


setx GROQ_API_KEY "your_api_key_here"


### Step 3: Run


python app.py


---

## 🧠 Why This Project Is Valuable

This project demonstrates:
- Production-grade prompt engineering
- Personal AI system design
- Identity-safe assistant behavior
- Resume-driven intelligence
- Real-world GenAI application patterns

Ideal for:
- AI Engineer portfolios
- GenAI interviews
- Personal AI copilots
- Teaching and mentoring systems

---

## 🔮 Future Enhancements

- Long-term memory using RAG
- Vector database integration
- Web or Streamlit UI
- Cloud deployment (Azure / GCP)
- Multi-agent personal AI ecosystem

---

## 🏁 Final Takeaway

You do not need fine-tuning to build powerful personal AI systems.  
You need **structure, clarity, and disciplined prompt design**.

This project is a clean, scalable foundation for a true **Digital Second Brain**
