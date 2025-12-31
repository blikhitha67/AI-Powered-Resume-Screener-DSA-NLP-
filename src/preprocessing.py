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
# This module cleans and normalizes resume and job description text
# before applying NLP algorithms.
# - Converts text to lowercase for consistency
# - Removes special characters and numbers using regular expressions
# - Uses spaCy to tokenize the text
# - Removes stopwords that do not add semantic meaning
# - Applies lemmatization to convert words to their base form
# The output is clean text that improves TF-IDF feature extraction
# and cosine similarity calculations.
