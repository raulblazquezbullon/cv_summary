# Automatic CV summarizer
Our main goal with this repo is to automatize some data extraction from CVs, in order to parse it to a more structured form of data.

## Target
**Main idea**: extract name, studies, previous jobs, etc. We hope to achieve it using some NLP techniques and **maybe** a free LLM (educational purposes).

## Authors
- Raúl Blázquez Bullón ([@raulblazquezbullon](https://github.com/raulblazquezbullon)).

## Requirements
To run the codes of this repo, you must run the following commands on your terminal (I strongly recommend using `virtualenv`):
```bash
pip install virtualenv
virtualenv <your-venv-name>
source <your-venv-name>/bin/activate
pip install -r requirements.txt
python3 -m spacy download en_core_web_sm
python3 -m spacy download es_core_news_sm
```
