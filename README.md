# 🧠 LLM-Powered Research Assistant

An intelligent research assistant that uses large language models (LLMs) via [LangChain](https://www.langchain.com/) to generate structured, tool-assisted summaries. Supports Claude (Anthropic) and OpenAI models, optionally with web search or other tools.

---

## 🚀 Features

- ✅ Structured responses with Pydantic formatting
- 🔧 Optional tool integration (e.g., web search)
- 🤖 Supports function-calling models (Claude, GPT-4o)
- 🔄 Switchable between Claude, OpenAI, and Groq models
- 📚 Output includes topic, summary, sources, and tools used

---

## 📦 Installation

Install required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
ANTHROPIC_API_KEY=your-claude-key
OPENAI_API_KEY=your-openai-key
GROQ_API_KEY=your-groq-key  # Optional
```

---

## 🧑‍💻 Usage

Run the assistant:

```bash
python main.py
```

Example interaction:
```
What can I help you with?
> impact of microplastics on marine life
```

---

## ✅ Output Format

```json
{
  "topic": "Microplastics",
  "summary": "Microplastics are tiny plastic fragments that ...",
  "sources": [
    "Scientific American",
    "NOAA",
    "UNEP Reports"
  ],
  "tools_used": ["search"]
}
```

---

## 🔁 Model Switching

### Claude (Recommended)
```python
from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(model="claude-3-opus-20240229")
```

### OpenAI
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o")
```

### Groq (no tools)
```python
from langchain_groq import ChatGroq
llm = ChatGroq(model="mixtral-8x7b-32768")
```

---

## 📁 Project Structure

```
.
├── main.py              # Main entry point
├── tools.py             # Tool definitions (e.g., search)
├── .env                 # API keys
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## 🧠 Use Cases

- Academic research summaries
- Blog and article prep
- Content idea exploration
- Writing assistants with sources

---

## 🧩 Dependencies

```text
langchain
langchain-anthropic
langchain-openai
langchain-groq
python-dotenv
```

---

## 🙏 Credits

- [LangChain](https://www.langchain.com/)
- [Anthropic Claude](https://www.anthropic.com/)
- [OpenAI](https://platform.openai.com/)
- [Groq Cloud](https://console.groq.com/)
- [Code_support](TechWhttps://www.youtube.com/@TechWithTimithTim)