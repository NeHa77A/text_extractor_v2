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
        words = [word for word in words if word.isalpha() and word.lower() not in self.stop_words]
        return ' '.join(words)

class DataProcessor:
    def __init__(self, input_folder="Artifact/DataExtraction", output_folder="Artifact/CleanData"):
        self.input_folder = input_folder
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)
        self.cleaner = TextCleaning()

    def process_files(self):
        files = os.listdir(self.input_folder)
        for file_name in files:
            if file_name.endswith('.txt'):
                input_path = os.path.join(self.input_folder, file_name)
                output_path = os.path.join(self.output_folder, file_name)
                self.process_file(input_path, output_path)

    def process_file(self, input_path, output_path):
        try:
            with open(input_path, 'r', encoding='utf-8') as infile:
                text = infile.read()
                cleaned_text = self.cleaner.clean_text(text)
                with open(output_path, 'w', encoding='utf-8') as outfile:
                    outfile.write(cleaned_text)
                print(f"Processed {input_path} and saved cleaned data to {output_path}")
        except Exception as e:
            print(f"Failed to process {input_path}: {e}")

if __name__ == "__main__":
    processor = DataProcessor()
    processor.process_files()
