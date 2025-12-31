import re
import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    return " ".join(tokens)

# How the Code Works:
# 1. This module cleans and normalizes resume and job description text
# 2. before applying NLP algorithms.
# 3. Converts text to lowercase for consistency
# 4. Removes special characters and numbers using regular expressions
# 5. Uses spaCy to tokenize the text
# 6. Removes stopwords that do not add semantic meaning
# 7. Applies lemmatization to convert words to their base form
# The output is clean text that improves TF-IDF feature extraction and cosine similarity calculations.
