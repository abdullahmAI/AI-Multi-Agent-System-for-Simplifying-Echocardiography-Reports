import os
from PyPDF2 import PdfReader

# === STEP 1: USER INPUT ===
pdf_path = "/home/deep/Desktop/Abdullah/KFSH-Reports/report_cleaned_2/401-319959.pdf"  # 👈 Change this to the user's file

# === STEP 2: Extract Patient Number ===
filename = os.path.basename(pdf_path)
patient_number = filename.split('-')[0].split('.')[0]  # Handles both '270.pdf' and '401-xxxx.pdf'

# === STEP 3: Extract Text from PDF ===
text = ""
try:
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        text += page.extract_text() or ""
    text = text.replace('\n', ' ').replace('\r', ' ').strip()
except Exception as e:
    print(f"⚠️ Error reading {pdf_path}: {e}")
    text = ""

# === STEP 4: Save to Variable for Agent ===
extracted_report = f"Patient number {patient_number}: {text}"
print("📄 Extracted Report:\n", extracted_report[:1000])  # preview only

import re

# 🔧 Arabic text cleaner (optional)
def clean_arabic_text(text):
    text = re.sub(r'[^\u0600-\u06FF0-9\s.,:؛\-\n\*]', '', text)
    text = re.sub(r'[.,]{2,}', '.', text)
    text = re.sub(r'[،]{2,}', '،', text)
    text = re.sub(r'\s{2,}', ' ', text)
    text = re.sub(r'\n{2,}', '\n', text)
    return text.strip()

def strip_thinking(text):
    """Remove any <think>...</think> blocks from the LLM output."""
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    
    extractor_agent_v3 = Agent(
    role="Cardiology Diagnostic Expert",
    goal="Extract all cardiac diseases from an echocardiography report",
    backstory="A seasoned cardiologist with expertise in interpreting echo reports and identifying heart diseases.",
    llm=llm,
    # verbose=True
)

storyteller_agent_v3 = Agent(
    role="Medical Storyteller for patients with no medical background",
    goal="Simplify medical content and turn it into engaging stories to let the patients understand what they are suffering from",
    backstory="A pediatric health educator skilled at explaining heart diagnoses to patients using metaphors and simple terms as a story.",
    llm=llm,
    # verbose=True
)

translator_agent_v3 = Agent(
    role="Arabic Medical Translator",
    goal="Translate English medical stories into clear, patient-friendly Arabic",
    backstory="A compassionate translator focused on making health education accessible to Arabic-speaking patients.",
    llm=llm,
    # verbose=True
)

task_diagnose_v3 = Task(
    name="extract_diagnosis_v3",
    description=(
    "You are a clinical cardiologist analyzing echocardiography reports. Your task is to extract all **diagnosed heart-related conditions**, such as valve diseases, heart failure, chamber abnormalities, and pulmonary hypertension.\n\n"
    "For each finding, list:\n"
    "1. **Disease Name** (e.g., aortic stenosis, pulmonary hypertension)\n"
    "2. **Severity** if available (mild, moderate, severe)\n"
    "3. **Short Explanation** for a medical summary\n\n"
    "Avoid restating echo measurements, ignore normal findings, and skip formatting like WMSI tables. Focus only on **what is abnormal and clinically relevant**.\n\n"
    "Report:\n{extracted_report}"
    ),
    expected_output="Aortic stenosis (severity): Short clinical explanation in English.",
    input_variables=["extracted_report"],
    agent=extractor_agent_v3
)

task_story_v3 = Task(
    name="story_for_kid_v3",
    description=(
        "You are a friendly medical educator telling a story to a patient with no medical background about their heart condition. \n\n"
        "Explain the diagnosed heart problems as a simple story, using easy words and everyday analogies. Imagine you are telling this to a child or a person who has never heard medical terms before.\n\n"
        "Keep it very short and clear, for example:\n\n"
        "\"The heart is like a busy house with doors that open and close to let blood flow. Sometimes, one door gets stiff or leaky, making the heart work harder. But doctors can help.\"\n\n"
        "Use this style to explain the following conditions:\n\n"
        "Do not use medical terms or complicated language. Make it warm, simple, and easy to understand."
    ),
    expected_output="A very simple, warm, and clear story that a patient with no medical background can understand.",
    agent=storyteller_agent_v3,
    input_variables=["extract_diagnosis_v3"],
    context=[task_diagnose_v3]
)

# task_story_v3 = Task(
#     name="story_for_kid_v3",
#     description=(
#     "You are a medical educator. Your task is to explain the diagnosed heart conditions in simple, direct English so a **patient with no medical background** can understand them.\n\n"
#     "For each condition, write:\n"
#     "1. The condition name (e.g., aortic stenosis)\n"
#     "2. A simple explanation (avoid medical terms)\n\n"
#     "Make the language clear and short. Don't add emotional tone or extra advice.\n"
#     ),
#     expected_output="Condition name and short explanation that non medical person able to understand it.",
#     input_variables=["extract_diagnosis_v3"],
#     agent=storyteller_agent_v3,
#     context=[task_diagnose_v3]
# )

task_translate_v3 = Task(
    name="arabic_translation_v3",
    description=(
        "Translate the following text from English to Arabic only.\n"
        "Do not change, summarize, or reword.\n"
        "Only return the translation in Arabic — no explanations, no extra languages, no comments.\n\n"
        
    ),
    expected_output="The exact Arabic translation of the input text.",
    agent=translator_agent_v3,
    context=[task_story_v3]
)

crew_v3 = Crew(
    agents=[extractor_agent_v3, storyteller_agent_v3, translator_agent_v3],
    tasks=[task_diagnose_v3, task_story_v3, task_translate_v3],
    # verbose=True
)

result_v3 = crew_v3.kickoff(inputs={"extracted_report": extracted_report})

# 🖨️ Show cleaned outputs
outputs_v3 = {
    task.name: clean_arabic_text(strip_thinking(task.raw.strip()))
    if "arabic" in task.name else strip_thinking(task.raw.strip())
    for task in result_v3.tasks_output
}

print("📌 Extracted Diagnosis:\n", outputs_v3.get("extract_diagnosis_v3", "No diagnosis found"))
print("\n🧒 Story for Patient (EN):\n", outputs_v3.get("story_for_kid_v3", "No story generated"))
print("\n🌍 Arabic Translation:\n", outputs_v3.get("arabic_translation_v3", "No Arabic translation"))
