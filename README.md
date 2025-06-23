# AI-Multi-Agent-System-for-Simplifying-Echocardiography-Reports

📌 Key Features
🔍 Automatic Diagnosis Extraction from echo reports (PDF format)

🧒 Patient-Friendly Story Generation using natural language storytelling

🌐 Arabic Translation of the simplified story

⚙️ Powered by Local AI (Ollama) and CrewAI Agents

🧠 Multi-Agent Workflow
Agent	Description
1. Extractor Agent	Takes the raw PDF echo report and extracts relevant diagnoses (e.g., aortic stenosis, mitral regurgitation)
2. Story Teller Agent	Transforms the diagnosis into a simple, relatable story for patients (non-expert level)
3. Translator Agent	Translates the simplified English story into Arabic for patient comprehension

🛠️ Technologies Used
Python

PyPDF2 – PDF parsing

CrewAI – Multi-agent orchestration

LangChain – LLM abstraction layer

Ollama – Local LLM runtime (deepseek-r1:70)

📁 Project Structure

```bash
📦 echo-simplifier
│
├── agents/
│   ├── extractor_agent.py
│   ├── storyteller_agent.py
│   └── translator_agent.py
│
├── pdf_parser/
│   └── extract_text.py
│
├── main.py              # Orchestrates the flow: PDF ➜ Diagnosis ➜ Story ➜ Arabic
├── requirements.txt
└── README.md
```
🚀 How to Run
Install dependencies
```
1- install ollama model locally into your device
2- ensure your GPU compatibility with the installed model
3- install CrewAI 
```
Make sure Ollama is running with the model

```bash
ollama run deepseek-r1:70
```
Run the main script
```bash
python main.py
```
📄 Example Output
Original Diagnosis (from PDF):

Severe mitral valve stenosis with mild aortic regurgitation.

🧒 Simplified Story:

Your heart has a doorway (the mitral valve) that is too narrow, making it hard for blood to flow properly. Another doorway (the aortic valve) is slightly leaky, but not too concerning. Imagine a house where one door is stuck and the other drips a little — it still works, but not perfectly.

🌐 Arabic Translation:

قلبك يحتوي على صمام (الصمام التاجي) ضيق جداً، مما يجعل تدفق الدم صعبًا. وصمام آخر (الصمام الأبهري) فيه تسريب بسيط، لكنه ليس خطيرًا. تخيل منزلاً بباب عالق وآخر يتسرب منه الماء قليلاً – لا يزال يعمل، ولكن ليس بشكل مثالي.



✨ Use Cases
Empowering patients with easy-to-understand health information

Enhancing doctor-patient communication

Local clinics without cloud AI services (offline Ollama integration)
