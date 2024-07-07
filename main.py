# import os
# from src.TextCleaning import *
# from src.SentimentAnalysis import *
# import pandas as pd
# from src.DataExtraction import *

# class DataProcessor:
#     def __init__(self, input_folder="Artifact/DataExtraction", input_file="input.xlsx", output_folder="Artifact/CleanData"):
#         self.input_folder = input_folder
#         self.input_file = input_file
#         self.output_folder = output_folder
#         os.makedirs(self.output_folder, exist_ok=True)
#         self.cleaner = TextCleaning()
#         self.sentiment_analyzer = SentimentAnalysis()

#     # def process_files(self):
#     #     if not os.path.exists(self.input_folder):
#     #         raise FileNotFoundError(f"The system cannot find the path specified: '{self.input_folder}'")
        
#     #     df = pd.read_excel(self.input_file)
        
#     #     for file_name in os.listdir(self.input_folder):
#     #         if file_name.endswith('.txt'):
#     #             url_id = os.path.splitext(file_name)[0]
#     #             input_path = os.path.join(self.input_folder, file_name)
#     #             output_path = os.path.join(self.output_folder, file_name)
#     #             self.process_file(input_path, output_path, df, url_id)
        
#     #     # Save updated DataFrame back to Excel
#     #     df.to_excel(self.input_file, index=False)
#     #     print(f"Sentiment, readability, and additional statistics updated in {self.input_file}")
#     def process_files(self):
#         files = os.listdir(self.input_folder)
#         for file_name in files:
#             if file_name.endswith('.txt'):
#                 input_path = os.path.join(self.input_folder, file_name)
#                 output_path = os.path.join(self.output_folder, file_name)
#                 self.process_file(input_path, output_path)

#     def process_file(self, input_path, output_path):
#         try:
#             with open(input_path, 'r', encoding='utf-8') as infile:
#                 text = infile.read()
#                 cleaned_text = self.cleaner.clean_text(text)
#                 with open(output_path, 'w', encoding='utf-8') as outfile:
#                     outfile.write(cleaned_text)
#                 print(f"Processed {input_path} and saved cleaned data to {output_path}")
#         except Exception as e:
#             print(f"Failed to process {input_path}: {e}")

#     def process_file(self, input_path, output_path, df, url_id):
#         try:
#             with open(input_path, 'r', encoding='utf-8') as infile:
#                 text = infile.read()
#                 cleaned_words = self.cleaner.clean_text(text)
#                 cleaned_text = ' '.join(cleaned_words)
                
#                 with open(output_path, 'w', encoding='utf-8') as outfile:
#                     outfile.write(cleaned_text)

#                 positive_score, negative_score, polarity_score, subjectivity_score = self.sentiment_analyzer.analyze_sentiment(cleaned_words)
#                 avg_sentence_length, percentage_complex_words, fog_index = self.sentiment_analyzer.readability_analysis(text, cleaned_words)
#                 word_count, syllable_count_per_word, avg_word_length = self.sentiment_analyzer.compute_statistics(cleaned_words)
#                 personal_pronouns_count = self.sentiment_analyzer.count_personal_pronouns(text)
                
#                 # Update DataFrame with sentiment analysis results
#                 idx = df.index[df['URL_ID'] == url_id].tolist()[0]
#                 df.at[idx, 'POSITIVE SCORE'] = positive_score
#                 df.at[idx, 'NEGATIVE SCORE'] = negative_score
#                 df.at[idx, 'POLARITY SCORE'] = polarity_score
#                 df.at[idx, 'SUBJECTIVITY SCORE'] = subjectivity_score
                
#                 # Update DataFrame with readability analysis results
#                 df.at[idx, 'AVG SENTENCE LENGTH'] = avg_sentence_length
#                 df.at[idx, 'PERCENTAGE OF COMPLEX WORDS'] = percentage_complex_words
#                 df.at[idx, 'FOG INDEX'] = fog_index
                
#                 # Update DataFrame with additional statistics
#                 df.at[idx, 'WORD COUNT'] = word_count
#                 df.at[idx, 'SYLLABLES PER WORD'] = syllable_count_per_word
#                 df.at[idx, 'AVG WORD LENGTH'] = avg_word_length
#                 df.at[idx, 'PERSONAL PRONOUNS'] = personal_pronouns_count

#                 print(f"Processed {input_path} and saved cleaned data to {output_path}")
#         except Exception as e:
#             print(f"Failed to process {input_path}: {e}")

# if __name__ == "__main__":
#     input_file = 'input.xlsx'  # Change this to your actual input file path
#     data_extraction = DataExtraction(input_file)
#     data_extraction.extract_articles()
#     processor = DataProcessor()
#     processor.process_files()


## Main.py
# import os
# import pandas as pd
# from src.TextCleaning import TextCleaning
# from src.SentimentAnalysis import SentimentAnalysis
# from src.DataExtraction import DataExtraction

# class DataProcessor:
#     def __init__(self, input_folder="Artifact/DataExtraction", input_file="input.xlsx", output_folder="Artifact/CleanData"):
#         self.input_folder = input_folder
#         self.input_file = input_file
#         self.output_folder = output_folder
#         os.makedirs(self.output_folder, exist_ok=True)
#         self.cleaner = TextCleaning()
#         self.sentiment_analyzer = SentimentAnalysis()

#     def process_files(self):
#         if not os.path.exists(self.input_folder):
#             raise FileNotFoundError(f"The system cannot find the path specified: '{self.input_folder}'")
        
#         df = pd.read_excel(self.input_file)
        
#         for file_name in os.listdir(self.input_folder):
#             if file_name.endswith('.txt'):
#                 url_id = os.path.splitext(file_name)[0]

#                 input_path = os.path.join(self.input_folder, file_name)
#                 output_path = os.path.join(self.output_folder, file_name)
#                 self.process_file(input_path, output_path, df, url_id)
        
#         # Save updated DataFrame back to Excel
#         df.to_excel(self.input_file, index=False)
#         print(f"Sentiment, readability, and additional statistics updated in {self.input_file}")

#     def process_file(self, input_path, output_path, df, url_id):
#         try:
#             with open(input_path, 'r', encoding='utf-8') as infile:
#                 text = infile.read()
#                 cleaned_text = self.cleaner.clean_text(text)
                
#                 with open(output_path, 'w', encoding='utf-8') as outfile:
#                     outfile.write(cleaned_text)

#                 positive_score, negative_score, polarity_score, subjectivity_score = self.sentiment_analyzer.analyze_sentiment(cleaned_text)
#                 avg_sentence_length, percentage_complex_words, fog_index = self.sentiment_analyzer.readability_analysis(text, cleaned_text)
#                 word_count, syllable_count_per_word, avg_word_length = self.sentiment_analyzer.compute_statistics(cleaned_text)
#                 personal_pronouns_count = self.sentiment_analyzer.count_personal_pronouns(text)
                
#                 # Update DataFrame with sentiment analysis results
#                 idx = df.index[df['URL_ID'] == url_id].tolist()[0]
#                 df.at[idx, 'POSITIVE SCORE'] = positive_score
#                 df.at[idx, 'NEGATIVE SCORE'] = negative_score
#                 df.at[idx, 'POLARITY SCORE'] = polarity_score
#                 df.at[idx, 'SUBJECTIVITY SCORE'] = subjectivity_score
                
#                 # Update DataFrame with readability analysis results
#                 df.at[idx, 'AVG SENTENCE LENGTH'] = avg_sentence_length
#                 df.at[idx, 'PERCENTAGE OF COMPLEX WORDS'] = percentage_complex_words
#                 df.at[idx, 'FOG INDEX'] = fog_index
                
#                 # Update DataFrame with additional statistics
#                 df.at[idx, 'WORD COUNT'] = word_count
#                 df.at[idx, 'SYLLABLES PER WORD'] = syllable_count_per_word
#                 df.at[idx, 'AVG WORD LENGTH'] = avg_word_length
#                 df.at[idx, 'PERSONAL PRONOUNS'] = personal_pronouns_count

#                 print(f"Processed {input_path} and saved cleaned data to {output_path}")
#         except Exception as e:
#             print(f"Failed to process {input_path}: {e}")

# if __name__ == "__main__":
#     input_file = 'input.xlsx'  # Change this to your actual input file path
#     data_extraction = DataExtraction(input_file)
#     data_extraction.extract_articles()
#     processor = DataProcessor()
#     processor.process_files()


# import os
# import pandas as pd
# from src.TextCleaning import TextCleaning
# from src.SentimentAnalysis import SentimentAnalysis
# from src.DataExtraction import DataExtraction

# class DataProcessor:
#     def __init__(self, input_folder="Artifact/DataExtraction", input_file="input.xlsx", output_folder="Artifact/CleanData"):
#         self.input_folder = input_folder
#         self.input_file = input_file
#         self.output_folder = output_folder
#         os.makedirs(self.output_folder, exist_ok=True)
#         self.cleaner = TextCleaning()
#         self.sentiment_analyzer = SentimentAnalysis()

#     def process_files(self, input_folder ="Artifact\CleanData"):
#         input_folder = self.input_folder
#         if not os.path.exists(input_folder):
#             raise FileNotFoundError(f"The system cannot find the path specified: '{self.input_folder}'")
        
#         df = pd.read_excel(self.input_file)
        
#         for file_name in os.listdir(self.input_folder):
#             if file_name.endswith('.txt'):
#                 url_id = os.path.splitext(file_name)[0]

#                 input_path = os.path.join(self.input_folder, file_name)
#                 output_path = os.path.join(self.output_folder, file_name)
#                 self.process_file(input_path, output_path, df, url_id)
        
#         # Save updated DataFrame back to Excel
#         df.to_excel(self.input_file, index=False)
#         print(f"Sentiment, readability, and additional statistics updated in {self.input_file}")

#     def process_file(self, input_path, output_path, df, url_id):
#         try:
#             with open(input_path, 'r', encoding='utf-8') as infile:
#                 text = infile.read()
#                 cleaned_text = self.cleaner.clean_text(text)
                
#                 with open(output_path, 'w', encoding='utf-8') as outfile:
#                     outfile.write(cleaned_text)

#                 positive_score, negative_score, polarity_score, subjectivity_score = self.sentiment_analyzer.analyze_sentiment(cleaned_text)
#                 avg_sentence_length, percentage_complex_words, fog_index = self.sentiment_analyzer.readability_analysis(text, cleaned_text)
#                 word_count, syllable_count_per_word, avg_word_length = self.sentiment_analyzer.compute_statistics(cleaned_text)
#                 personal_pronouns_count = self.sentiment_analyzer.count_personal_pronouns(text)
                
#                 # Update DataFrame with sentiment analysis results
#                 idx = df.index[df['URL_ID'] == url_id].tolist()[0]
#                 df.at[idx, 'POSITIVE SCORE'] = positive_score
#                 df.at[idx, 'NEGATIVE SCORE'] = negative_score
#                 df.at[idx, 'POLARITY SCORE'] = polarity_score
#                 df.at[idx, 'SUBJECTIVITY SCORE'] = subjectivity_score
                
#                 # Update DataFrame with readability analysis results
#                 df.at[idx, 'AVG SENTENCE LENGTH'] = avg_sentence_length
#                 df.at[idx, 'PERCENTAGE OF COMPLEX WORDS'] = percentage_complex_words
#                 df.at[idx, 'FOG INDEX'] = fog_index
                
#                 # Update DataFrame with additional statistics
#                 df.at[idx, 'WORD COUNT'] = word_count
#                 df.at[idx, 'SYLLABLES PER WORD'] = syllable_count_per_word
#                 df.at[idx, 'AVG WORD LENGTH'] = avg_word_length
#                 df.at[idx, 'PERSONAL PRONOUNS'] = personal_pronouns_count

#                 print(f"Processed {input_path} and saved cleaned data to {output_path}")
#         except Exception as e:
#             print(f"Failed to process {input_path}: {e}")

# if __name__ == "__main__":
#     input_file = 'input.xlsx'  # Change this to your actual input file path
#     data_extraction = DataExtraction(input_file)
#     data_extraction.extract_articles()
#     processor = DataProcessor()
#     processor.process_files()

import os
import pandas as pd
from src.TextCleaning import TextCleaning
from src.SentimentAnalysis import SentimentAnalysis
from src.DataExtraction import DataExtraction
from src.constant import *

class DataProcessor:
    def __init__(self, input_folder=OUTPUT_FOLDER_EXTRACTION, input_file=OUTPUT_FILE, output_folder=OUTPUT_FOLDER_CLEAN):
        self.input_folder = input_folder
        self.input_file = input_file
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)
        self.cleaner = TextCleaning()
        self.sentiment_analyzer = SentimentAnalysis()

    def process_files(self, input_folder =OUTPUT_FOLDER_CLEAN):
        input_folder = self.input_folder
        if not os.path.exists(input_folder):
            raise FileNotFoundError(f"The system cannot find the path specified: '{self.input_folder}'")
        
        df = pd.read_excel(self.input_file)
        
        for file_name in os.listdir(self.input_folder):
            if file_name.endswith('.txt'):
                url_id = os.path.splitext(file_name)[0]

                input_path = os.path.join(self.input_folder, file_name)
                output_path = os.path.join(self.output_folder, file_name)
                self.process_file(input_path, output_path, df, url_id)
        
        # Save updated DataFrame back to Excel
        df.to_excel(self.input_file, index=False)
        print(f"Sentiment, readability, and additional statistics updated in {self.input_file}")

    def process_file(self, input_path, output_path, df, url_id):
        try:
            with open(input_path, 'r', encoding='utf-8') as infile:
                text = infile.read()
                cleaned_text = self.cleaner.clean_text(text)
                
                with open(output_path, 'w', encoding='utf-8') as outfile:
                    outfile.write(" ".join(cleaned_text))  # Write cleaned text as a single string

                positive_score, negative_score, polarity_score, subjectivity_score = self.sentiment_analyzer.analyze_sentiment(cleaned_text)
                avg_sentence_length, percentage_complex_words, fog_index = self.sentiment_analyzer.readability_analysis(text)
                word_count, syllable_count_per_word, avg_word_length = self.sentiment_analyzer.compute_statistics(cleaned_text)
                personal_pronouns_count = self.sentiment_analyzer.count_personal_pronouns(text)
                # extra
                avg_words_per_sentence = self.sentiment_analyzer.average_words_per_sentence(text)
                complex_word_count = self.sentiment_analyzer.count_complex_words(text)
                syllables_per_word = self.sentiment_analyzer.count_syllables_per_word(text)

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

                
                # Update DataFrame with additional metrics
                #df.at[idx, 'AVG WORDS PER SENTENCE'] = avg_words_per_sentence
                df.at[idx, 'COMPLEX WORD COUNT'] = complex_word_count
                #df.at[idx, 'SYLLABLES PER WORD'] = syllables_per_word
                


                print(f"Processed {input_path} and saved cleaned data to {output_path}")
        except Exception as e:
            print(f"Failed to process {input_path}: {e}")

if __name__ == "__main__":
    input_file = INPUT_FILE  # Change this to your actual input file path
    data_extraction = DataExtraction(input_file)
    data_extraction.extract_articles()
    processor = DataProcessor()
    processor.process_files()

