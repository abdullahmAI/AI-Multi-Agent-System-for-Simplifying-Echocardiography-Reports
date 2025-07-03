# AI-Multi-Agent-System for Simplifying Echocardiography Reports
This project implements a complete agent based AI system that transforms complex echocardiography (echo) reports in PDF format into simplified, patient-friendly narratives in both English and Arabic. Built with a focus on privacy, local deployment, and real-world clinical utility, the system demonstrates practical integration of multi-agent orchestration, prompt engineering, and offline large language models (LLMs).


## Key Features:
 
- Automatic extraction of medical diagnoses from PDF-formatted echo reports

- Natural language storytelling to simplify medical jargon for non-expert patients

- Arabic translation of the simplified explanation

- Fully local execution using Ollama and custom LLMs

- Prompt-driven agent collaboration using CrewAI

 ## System Architecture:
 
This system follows a modular multi-agent architecture. Each agent operates independently, collaborating through a shared task pipeline.

## Agents:

1- ExtractorAgent
Identifies and extracts relevant clinical findings (e.g., aortic regurgitation, mitral stenosis) from echo report PDFs.

2- StoryTellerAgent
Converts the diagnosis into a simple, metaphor-rich narrative a non-medical reader can understand.

3- TranslatorAgent
Translates the English story into fluent, culturally adapted Arabic.

Each agent is implemented with structured prompt templates, using local LLM inference for consistency and privacy.



## Technologies Used:
 
- Python

- PyPDF2 – PDF parsing

- CrewAI – Agent orchestration

- LangChain – Prompt templating and abstraction

- Ollama – Local LLM runtime (tested with deepseek-r1:70b)

## Project Structure

```bash
 echo-simplifier
│
├── agents/
│   ├── extractor_agent
│   ├── storyteller_agent
│   └── translator_agent
│
├── pdf_parser/
│   └── extract_text
│
├── main.py              
├── requirements.txt
└── README.md
```
 ## How to Run:
Install dependencies
```
1- install ollama model locally into your device
2- ensure your GPU compatibility with the installed model
3- install CrewAI 
```
Make sure Ollama is running with the model

```bash
ollama run deepseek-r1:70b
```
Run the main script
```bash
agents.py ( if you will use terminal)
or
run the notebook directly
```
 ## Example Output:
- Original Diagnosis (from PDF):

Severe mitral valve stenosis with mild aortic regurgitation.

 - Simplified Story:

Your heart has a doorway (the mitral valve) that is too narrow, making it hard for blood to flow properly. Another doorway (the aortic valve) is slightly leaky, but not too concerning. Imagine a house where one door is stuck and the other drips a little but it still works, but not perfectly.

- Arabic Translation:

قلبك يحتوي على صمام (الصمام التاجي) ضيق جداً، مما يجعل تدفق الدم صعبًا. وصمام آخر (الصمام الأبهري) فيه تسريب بسيط، لكنه ليس خطيرًا. تخيل منزلاً بباب عالق وآخر يتسرب منه الماء قليلاً – لا يزال يعمل، ولكن ليس بشكل مثالي.



 ## Use Cases:
 
- Empowering patients with easy-to-understand health information

- Enhancing doctor-patient communication

- Local clinics without cloud AI services (offline Ollama integration)

## Highlights:

- Built an end-to-end agentic AI system grounded in real clinical documents

- Applied structured prompt engineering to guide agent output behavior

- Integrated offline LLMs via Ollama to preserve data privacy and control

- Modular codebase ready for extension to other clinical domains or languages

  ## Future Directions:
  
- Support for multilingual output beyond Arabic

- Integration with OCR for scanned (non-digital) PDFs

- Deployment via GUI for clinical use

- Fine-tuning agents using synthetic feedback loops
