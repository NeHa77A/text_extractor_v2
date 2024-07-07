# import os
# import pandas as pd
# from nltk.tokenize import word_tokenize, sent_tokenize
# from nltk.corpus import stopwords
# import nltk
# import re

# nltk.download('punkt')
# nltk.download('stopwords')

# class SentimentAnalysis:
#     def __init__(self):
#         self.positive_words = set(['good', 'happy', 'positive', 'fortunate', 'correct', 'superior', 'excellent', 'great', 'best', 'wonderful'])
#         self.negative_words = set(['bad', 'sad', 'negative', 'unfortunate', 'wrong', 'inferior', 'terrible', 'horrible', 'worst', 'awful'])
#         self.stop_words = set(stopwords.words('english'))
    
#     def clean_text(self, text):
#         words = word_tokenize(text)
#         words = [word.lower() for word in words if word.isalpha() and word.lower() not in self.stop_words]
#         return words
    
#     def analyze_sentiment(self, words):
#         positive_score = sum(1 for word in words if word in self.positive_words)
#         negative_score = sum(1 for word in words if word in self.negative_words)
#         polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
#         subjectivity_score = (positive_score + negative_score) / (len(words) + 0.000001)
#         return positive_score, negative_score, polarity_score, subjectivity_score
    
#     def readability_analysis(self, text, words):
#         sentences = sent_tokenize(text)
#         avg_sentence_length = len(words) / len(sentences) if sentences else 0
#         complex_words = [word for word in words if len(word) > 2]
#         percentage_complex_words = len(complex_words) / len(words) if words else 0
#         fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
#         return avg_sentence_length, percentage_complex_words, fog_index
    
#     def compute_statistics(self, words):
#         word_count = len(words)
#         syllable_count_per_word = sum([sum(1 for char in word if char in 'aeiou') for word in words]) / word_count if word_count else 0
#         avg_word_length = sum(len(word) for word in words) / word_count if word_count else 0
#         return word_count, syllable_count_per_word, avg_word_length

#     def count_personal_pronouns(self, text):
#         personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.I))
#         return personal_pronouns
# import os
# import pandas as pd
# from nltk.tokenize import word_tokenize, sent_tokenize
# from nltk.corpus import stopwords
# import nltk
# import re

# nltk.download('punkt')
# nltk.download('stopwords')

# class SentimentAnalysis:
#     def __init__(self):
#         self.positive_words = set(['good', 'happy', 'positive', 'fortunate', 'correct', 'superior', 'excellent', 'great', 'best', 'wonderful'])
#         self.negative_words = set(['bad', 'sad', 'negative', 'unfortunate', 'wrong', 'inferior', 'terrible', 'horrible', 'worst', 'awful'])
#         self.stop_words = set(stopwords.words('english'))
    
#     def clean_text(self, text):
#         words = word_tokenize(text)
#         cleaned_words = [word.lower() for word in words if word.isalpha() and word.lower() not in self.stop_words]
#         return cleaned_words
    
#     def analyze_sentiment(self, text):
#         cleaned_words = self.clean_text(text)
#         positive_score = sum(1 for word in cleaned_words if word in self.positive_words)
#         negative_score = sum(1 for word in cleaned_words if word in self.negative_words)
#         polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
#         subjectivity_score = (positive_score + negative_score) / (len(cleaned_words) + 0.000001)
#         return positive_score, negative_score, polarity_score, subjectivity_score
    
#     # def readability_analysis(self, text):
#     #     cleaned_words = self.clean_text(text)
#     #     sentences = sent_tokenize(text)
#     #     avg_sentence_length = len(cleaned_words) / len(sentences) if sentences else 0
#     #     complex_words = [word for word in cleaned_words if len(word) > 2]
#     #     percentage_complex_words = len(complex_words) / len(cleaned_words) if cleaned_words else 0
#     #     fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
#     #     return avg_sentence_length, percentage_complex_words, fog_index
#     def readability_analysis(self, text):
#         cleaned_words = self.clean_text(text)
#         sentences = sent_tokenize(text)
#         avg_sentence_length = len(cleaned_words) / len(sentences) if sentences else 0
#         complex_words = [word for word in cleaned_words if len(word) > 2]
#         percentage_complex_words = (len(complex_words) / len(cleaned_words)) * 100 if cleaned_words else 0
#         fog_index = 0.4 * (avg_sentence_length + (percentage_complex_words / 100))
#         return avg_sentence_length, percentage_complex_words, fog_index
    
#     def compute_statistics(self, text):
#         cleaned_words = self.clean_text(text)
#         word_count = len(cleaned_words)
#         syllable_count_per_word = sum([self.count_syllables(word) for word in cleaned_words]) / word_count if word_count else 0
#         avg_word_length = sum(len(word) for word in cleaned_words) / word_count if word_count else 0
#         return word_count, syllable_count_per_word, avg_word_length
    
#     def count_personal_pronouns(self, text):
#         personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.I))
#         return personal_pronouns
    
#     def count_syllables(self, word):
#         word = word.lower()
#         syllables = 0
#         vowels = "aeiou"
#         if word[0] in vowels:
#             syllables += 1
#         for index in range(1, len(word)):
#             if word[index] in vowels and word[index - 1] not in vowels:
#                 syllables += 1
#         if word.endswith("e"):
#             syllables -= 1
#         if syllables == 0:
#             syllables += 1
#         return syllables

import os
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, cmudict
import nltk
import re

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('cmudict')

class SentimentAnalysis:
    def __init__(self):
        self.positive_words = set(['good', 'happy', 'positive', 'fortunate', 'correct', 'superior', 'excellent', 'great', 'best', 'wonderful'])
        self.negative_words = set(['bad', 'sad', 'negative', 'unfortunate', 'wrong', 'inferior', 'terrible', 'horrible', 'worst', 'awful'])
        self.stop_words = set(stopwords.words('english'))
        self.syllable_dict = cmudict.dict()
    
    def clean_text(self, text):
        words = word_tokenize(text)
        cleaned_words = [word.lower() for word in words if word.isalpha() and word.lower() not in self.stop_words]
        return cleaned_words
    
    def calculate_positive_score(self, text):
        words = text.split()
        positive_score = sum(1 for word in words if word in self.positive_words)
        return positive_score
    
    def calculate_negative_score(self, text):
        words = text.split()
        negative_score = sum(1 for word in words if word in self.negative_words)
        return negative_score

    def analyze_sentiment(self, text):
        positive_score = self.calculate_positive_score(text)
        negative_score = self.calculate_negative_score(text)
        polarity_score = self.calculate_polarity_score(positive_score, negative_score)
        subjectivity_score = self.calculate_subjectivity_score(positive_score, negative_score, len(word_tokenize(text))) * 100
        return positive_score, negative_score, polarity_score, subjectivity_score
    
    def calculate_polarity_score(self, positive_score, negative_score):
        polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
        return polarity_score

    def calculate_subjectivity_score(self, positive_score, negative_score, total_words):
        subjectivity_score = (positive_score + negative_score) / (total_words + 0.000001)
        return subjectivity_score

    def readability_analysis(self, text):
        cleaned_words = self.clean_text(text)
        sentences = sent_tokenize(text)
        avg_sentence_length = len(cleaned_words) / len(sentences) if sentences else 0
        num_complex_words = self.count_complex_words(text)
        percentage_complex_words = (num_complex_words / len(cleaned_words)) * 100 if cleaned_words else 0
        fog_index = self.calculate_fog_index(avg_sentence_length, percentage_complex_words)
        return avg_sentence_length, percentage_complex_words, fog_index
    
    def calculate_fog_index(self, average_sentence_length, percentage_complex_words):
        fog_index = 0.4 * (average_sentence_length + (percentage_complex_words / 100))
        return fog_index
    
    def count_syllables(self, word):
        if word.lower() not in self.syllable_dict:
            return 0
        return [len(list(y for y in x if y[-1].isdigit())) for x in self.syllable_dict[word.lower()]][0]
    
    def is_complex(self, word):
        syllable_count = self.count_syllables(word)
        return syllable_count > 2

    def count_complex_words(self, text):
        words = nltk.word_tokenize(text)
        num_complex_words = sum(self.is_complex(word) for word in words)
        return num_complex_words

    def count_syllables_per_word(self, text):
        words = nltk.word_tokenize(text)
        syllable_counts = [self.count_syllables(word) for word in words]
        return syllable_counts

    def compute_statistics(self, text):
        cleaned_words = self.clean_text(text)
        word_count = len(cleaned_words)
        syllable_count_per_word = sum([self.count_syllables(word) for word in cleaned_words]) / word_count if word_count else 0
        avg_word_length = sum(len(word) for word in cleaned_words) / word_count if word_count else 0
        return word_count, syllable_count_per_word, avg_word_length
    
    def count_personal_pronouns(self, text):
        pattern = r"\b(I|we|my|ours|us)\b"
        pattern = r"(?<!\bUS\b)" + pattern
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        count = len(matches)
        return count
    
    def calculate_avg_word_length(self, text):
        words = text.split()
        total_characters = sum(len(word) for word in words)
        num_words = len(words)
        avg_word_length = total_characters / num_words
        return avg_word_length
    
    def average_words_per_sentence(self, text):
        sentences = sent_tokenize(text)
        num_sentences = len(sentences)
        if num_sentences == 0:
            return 0
        num_words = len(word_tokenize(text))
        avg_words_per_sentence = num_words / num_sentences
        return avg_words_per_sentence

    def count_complex_words(self, text):
        words = nltk.word_tokenize(text)
        num_complex_words = sum(self.is_complex(word) for word in words)
        return num_complex_words

    def count_syllables_per_word(self, text):
        words = nltk.word_tokenize(text)
        syllable_counts = [self.count_syllables(word) for word in words]
        return syllable_counts
    
