
# 🤖 AI Assistant – LLM Agent (LiveKit + OpenAI)

Text 💬 & (optional) voice 🎤 AI assistant built with LiveKit Agents and OpenAI.  
Includes a minimal agent, tool calls (weather 🌦️, promptifier 📝, embeddings 🧩), a CLI chat 💻, and full test harness ✅.

---

## ✨ Features
- 🤝 Friendly assistant with clear, grounded responses
- 🔧 Tools:
  - `lookup_weather(location)` – mocked in tests 🌤️
  - `promptify_text(raw_text)` – cleans user utterances into prompts 📝
  - `embed_text(raw_text)` – creates embeddings (OpenAI) 🧠
- 🚀 Three ways to run:
  1. 🧪 **Automated tests** (CI-friendly)
  2. 💻 **Local console chat**
  3. 🎙️ **(Optional)** LiveKit voice pipeline

---

## 🛠️ Tech Stack
- 🐍 Python 3.11
- 🟣 LiveKit Agents SDK
- 🔑 OpenAI (LLM + embeddings)
- 🧪 PyTest (+ asyncio)

---

## 📂 Repo Structure
```

.
├─ agent/
│  ├─ **init**.py
│  ├─ assistant.py        # Agent logic + tools
│  └─ run\_agent.py        # Console runner (python -m agent.run\_agent console)
├─ tests/
│  └─ test\_agent.py       # 7 tests covering messages + tool calls
├─ talk.py                # Minimal console chat (no LiveKit room)
├─ pytest.ini
└─ LICENSE

````

---

## ⚡ Quick Start

### 1️⃣ Create a virtual environment
```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -U pip
````

### 2️⃣ Install dependencies

```bash
pip install livekit-agents livekit-plugins-openai anyio pytest pytest-asyncio python-dotenv
```

### 3️⃣ Set environment variables

Create `.env.local` in the repo root (or export in your shell):

```
OPENAI_API_KEY=sk-...
# Optional (voice/LiveKit path only):
# LIVEKIT_URL=wss://your-project.livekit.cloud
# LIVEKIT_API_KEY=...
# LIVEKIT_API_SECRET=...
```

---

## ▶️ Run Options

### 🧪 A) Automated tests (recommended sanity check)

```bash
pytest -sv
```

✅ You should see **7 passed**.

### 💻 B) Console chat (simple text loop)

```bash
python talk.py
```

Type a message (e.g., `Hello`, `What's the weather in Tokyo?`, or `make lpr with yolo v8 and ros2`).

### 🎤 C) Voice pipeline with LiveKit

```bash
python -m agent.run_agent console
```

If you wire up LiveKit STT/TTS/turn detection in your agent entrypoint:

1. ⚙️ Set `LIVEKIT_*` env vars in `.env.local`
2. ▶️ Start your agent process (e.g., a worker or entry script that joins a LiveKit room)

> ℹ️ This template currently focuses on text & tests. Voice is easy to add later with LiveKit plugins.

---

## 📜 License

MIT – see [LICENSE](./LICENSE).

```


# 👩‍💻 Chaithra Lokasara Mahadevaswamy 

**AI Enthusiast | 🧠 Data Alchemist | 🚀 Innovation Seeker | 🌟 AI Researcher**  
*Building Tomorrow with Intelligence Today*

📍 Chang Gung University, Taipei, Taiwan  
🔗 [LinkedIn](https://www.linkedin.com/in/chaithra-lokasara-mahadevaswamy-5bb076214/)  
🤝 500+ Connections




