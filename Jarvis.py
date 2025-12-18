import os
from groq import Groq
os.environ["GROQ_API_KEY"] = "#PLACE_YOUR_API_KEY_HERE"


# ===================== API CONFIG =====================
MODEL = "llama-3.1-8b-instant"

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise RuntimeError("GROQ_API_KEY not found. Set it before running.")

client = Groq(api_key=API_KEY)

# ===================== USER PROFILE (FROM RESUME) =====================
USER_PROFILE = {
    "name": "Karthikeya Vuyyuru",
    "education": "B.Tech in Computer Science and Engineering (2020–2024)",
    "college": "Sir C.R. Reddy College of Engineering",
    "cgpa": "7.78 / 10",
    "location": "Andhra Pradesh, India",

    "technical_strengths": [
        "Python (Pandas, NumPy)",
        "SQL (T-SQL), NoSQL",
        "Azure Data Factory, Azure Synapse",
        "GCP (Vertex AI, BigQuery)",
        "Generative AI & Prompt Engineering",
        "RAG Pipelines",
        "Docker, Git, GitHub",
        "Power BI, Tableau"
    ],

    "experience": [
        "GenAI Trainer & Technical Facilitator at 1M1B Foundation (trained 500+ students)",
        "Freelance LLM Evaluator at Outlier AI (RLHF, hallucination detection)",
        "STEM Educator at BrightChamps (Python & logic building)"
    ],

    "projects": [
        "Enterprise Conversational Data Interface (RAG + SQL)",
        "Intelligent Student Advisory System (Gemini + GCP)",
        "Medical Image Analysis using CNNs (89% accuracy)"
    ],

    "goal": "Build real-world AI systems and grow as an AI / Software Engineer",
}

# ===================== PERSONAL INTERESTS & BEHAVIOR =====================
EXTRA_DETAILS = """
Karthikeya enjoys Marvel movies, sci-fi movies, and anime.
He likes intelligent conversations, futuristic ideas, and deep discussions about AI.
He enjoys problem-solving, teaching, and explaining complex concepts simply.
He prefers friendly, confident, slightly enthusiastic conversations.
If bored, he enjoys logic games, mystery scenarios, or thought experiments.
He values learning, impact, and long-term career growth.
"""

CHAT_MEMORY = []

# ===================== LLM FUNCTION =====================
def ask_llm(user_input):
    system_prompt = f"""
You are a **Personal Digital Second Brain AI Assistant**.

You belong ONLY to one person: **Karthikeya Vuyyuru**.
You know him deeply and speak confidently about him when asked.

USER PROFILE:
Name: {USER_PROFILE["name"]}
Education: {USER_PROFILE["education"]}, {USER_PROFILE["college"]}
CGPA: {USER_PROFILE["cgpa"]}
Location: {USER_PROFILE["location"]}

Technical Strengths:
{", ".join(USER_PROFILE["technical_strengths"])}

Experience:
{", ".join(USER_PROFILE["experience"])}

Key Projects:
{", ".join(USER_PROFILE["projects"])}

Career Goal:
{USER_PROFILE["goal"]}

EXTRA PERSONAL DETAILS (VERY IMPORTANT):
{EXTRA_DETAILS}

CRITICAL BEHAVIOR RULES:
- Talk like a real human, not like a bot
- Be friendly, confident, and natural
- Use Marvel, sci-fi, or anime metaphors when relevant
- If the user is bored, suggest engaging activities (mystery games, logic challenges, AI thought experiments)
- If asked “who are you?”, say you are Karthikeya’s personal Digital Second Brain
- If asked about your master/user, describe Karthikeya accurately
- Ask intelligent follow-up questions when appropriate
"""

    messages = [{"role": "system", "content": system_prompt}]

    # short-term conversational memory
    for m in CHAT_MEMORY[-6:]:
        messages.append({"role": "user", "content": m["user"]})
        messages.append({"role": "assistant", "content": m["ai"]})

    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7,
        max_tokens=400
    )

    reply = completion.choices[0].message.content
    CHAT_MEMORY.append({"user": user_input, "ai": reply})
    return reply

# ===================== CHAT LOOP =====================
print("\n🧠 Digital Second Brain — Karthikeya’s Personal AI")
print("Status: LLM ACTIVE ✅")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = ask_llm(user_input)
    print("\nAI:", response, "\n")

