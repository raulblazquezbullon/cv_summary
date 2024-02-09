# coding: utf-8

# Imports
import os
import logging
# import pytesseract # OCR library
import fitz
import spacy

# Logging configuration
log_dir = "../data/logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

num_logs = len([f for f in os.listdir(log_dir) if f.endswith(".log")])
log_file = f"{log_dir}/cv_summary_{num_logs}.log"
logging.basicConfig(
    level=logging.INFO,
    filename=log_file,
    filemode='w',
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Load CV
cv_file = "../data/inputs/CV_estudiante_microthali (1).pdf"
with fitz.open(cv_file) as f:
    text = ""
    for page in f:
        text += page.get_text()

print(text)

# Process with spaCy
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

# Extract entities
entities = []
for ent in doc.ents:
    entities.append((ent.text, ent.label_))
    print(ent.text, ent.label_)
    logging.info(f"{ent.text} : {ent.label_}")

# Extra info (profile photo, etc.)
