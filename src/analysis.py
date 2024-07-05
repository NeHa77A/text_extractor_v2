import os
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk
import re
nltk.download('punkt')
nltk.download('stopwords')

class SentimentAnalysis:
    def __init__(self):
        self.positive_words = set(['good', 'happy', 'positive', 'fortunate', 'correct', 'superior', 'excellent', 'great', 'best', 'wonderful'])
        self.negative_words = set(['bad', 'sad', 'negative', 'unfortunate', 'wrong', 'inferior', 'terrible', 'horrible', 'worst', 'awful'])
        self.stop_words = set(stopwords.words('english'))
    
    def clean_text(self, text):
        words = word_tokenize(text)
        words = [word.lower() for word in words if word.isalpha() and word.lower() not in self.stop_words]
        return words
    
    def analyze_sentiment(self, words):
        positive_score = sum(1 for word in words if word in self.positive_words)
        negative_score = sum(1 for word in words if word in self.negative_words)
        polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
        subjectivity_score = (positive_score + negative_score) / (len(words) + 0.000001)
        return positive_score, negative_score, polarity_score, subjectivity_score
    
    
def readability_analysis(text, words):
    sentences = sent_tokenize(text)
    avg_sentence_length = len(words) / len(sentences) if sentences else 0
    complex_words = [word for word in words if len(word) > 2]
    percentage_complex_words = len(complex_words) / len(words) if words else 0
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    return avg_sentence_length, percentage_complex_words, fog_index


def compute_statistics(words):
    word_count = len(words)
    syllable_count_per_word = sum([sum(1 for char in word if char in 'aeiou') for word in words]) / word_count if word_count else 0
    avg_word_length = sum(len(word) for word in words) / word_count if word_count else 0
    return word_count, syllable_count_per_word, avg_word_length

def count_personal_pronouns(text):
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.I))
    return personal_pronouns

class DataProcessor:
    def __init__(self, input_folder="Artifact/CleanData", input_file="input.xlsx"):
        self.input_folder = input_folder
        self.input_file = input_file
        self.sentiment_analyzer = SentimentAnalysis()
    
    def process_files(self):
        df = pd.read_excel(self.input_file)
        
        for file_name in os.listdir(self.input_folder):
            if file_name.endswith('.txt'):
                url_id = os.path.splitext(file_name)[0]
                input_path = os.path.join(self.input_folder, file_name)
                with open(input_path, 'r', encoding='utf-8') as infile:
                    text = infile.read()
                    cleaned_words = self.sentiment_analyzer.clean_text(text)
                    positive_score, negative_score, polarity_score, subjectivity_score = self.sentiment_analyzer.analyze_sentiment(cleaned_words)
                    
                    avg_sentence_length, percentage_complex_words, fog_index = readability_analysis(text, cleaned_words)
                    
                    # Compute additional statistics
                    word_count, syllable_count_per_word, avg_word_length = compute_statistics(cleaned_words)
                    personal_pronouns_count = count_personal_pronouns(text)
                    
                    # Update DataFrame with sentiment analysis results
                    idx = df.index[df['URL_ID'] == url_id].tolist()[0]
                    df.at[idx, 'POSITIVE SCORE'] = positive_score
                    df.at[idx, 'NEGATIVE SCORE'] = negative_score
                    df.at[idx, 'POLARITY SCORE'] = polarity_score
                    df.at[idx, 'SUBJECTIVITY SCORE'] = subjectivity_score
                    
                    # Update DataFrame with readability analysis results
                    df.at[idx, 'AVG SENTENCE LENGTH'] = avg_sentence_length
                    df.at[idx, 'PERCENTAGE OF COMPLEX WORDS'] = percentage_complex_words
                    df.at[idx, 'FOG INDEX'] = fog_index
                    
                    # Update DataFrame with additional statistics
                    df.at[idx, 'WORD COUNT'] = word_count
                    df.at[idx, 'SYLLABLES PER WORD'] = syllable_count_per_word
                    df.at[idx, 'AVG WORD LENGTH'] = avg_word_length
                    df.at[idx, 'PERSONAL PRONOUNS'] = personal_pronouns_count
        
        # Save updated DataFrame back to Excel
        df.to_excel(self.input_file, index=False)
        print(f"Sentiment, readability, and additional statistics updated in {self.input_file}")

if __name__ == "__main__":
    processor = DataProcessor()
    processor.process_files()
