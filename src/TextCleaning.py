import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

class TextCleaning:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
    
    def clean_text(self, text):
        words = word_tokenize(text)
        words = [word for word in words if (word.isalpha() or word == '.') and word.lower() not in self.stop_words]
        return ' '.join(words)
