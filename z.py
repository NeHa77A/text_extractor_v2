# import os
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# class DataExtraction:
#     def __init__(self, input_file, output_folder="Artifact"):
#         self.input_file = input_file
#         self.output_folder = output_folder
#         # Create the output folder if it does not exist
#         os.makedirs(self.output_folder, exist_ok=True)
    
#     def extract_text(self, url):
#         try:
#             response = requests.get(url)
#             soup = BeautifulSoup(response.content, 'html.parser')
#             title = soup.find('title').get_text()
#             article = ' '.join([p.get_text() for p in soup.find_all('p')])
#             return title + '\n' + article
#         except Exception as e:
#             print(f"Failed to extract {url}: {e}")
#             return ""

#     def extract_articles(self):
#         df = pd.read_excel(self.input_file)
#         for index, row in df.iterrows():
#             url_id = row['URL_ID']
#             url = row['URL']
#             print(f"Extracting URL_ID: {url_id} from {url}")
#             article_text = self.extract_text(url)
#             if article_text:
#                 output_path = os.path.join(self.output_folder, f"{url_id}.txt")
#                 with open(output_path, 'w', encoding='utf-8') as file:
#                     file.write(article_text)
#             else:
#                 print(f"No content extracted from {url}")

# if __name__ == "__main__":
#     input_file = 'input.xlsx'  # Change this to your actual input file path
#     data_extraction = DataExtraction(input_file)
#     data_extraction.extract_articles()

# import os
# import time
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import NoSuchElementException, WebDriverException

# class DataExtraction:
#     def __init__(self, input_file, output_folder="Artifacts"):
#         self.input_file = input_file
#         self.output_folder = output_folder
#         os.makedirs(self.output_folder, exist_ok=True)
        
#         # Initialize the Selenium WebDriver
#         options = Options()
#         options.add_argument("--headless")  # Run in headless mode
#         options.add_argument("--disable-gpu")
#         options.add_argument("--no-sandbox")
        
#         # Set path to the ChromeDriver executable
#         chrome_driver_path = 'chromedriver.exe'  # Update this path
#         self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
#     def extract_text(self, url):
#         try:
#             self.driver.get(url)
#             time.sleep(2)  # Wait for the page to load
            
#             #header = self.driver.find_element(By.CLASS_NAME, 'entry-title').text
#             header = self.driver.find_element(By.XPATH, '//h1[@class="entry-title"]').text
#             content = self.driver.find_element(By.CLASS_NAME, 'td-post-content.tagdiv-type').text
            
#             return header + '\n' + content
#         except (NoSuchElementException, WebDriverException) as e:
#             print(f"Failed to extract {url}: {e}")
#             return ""
    
#     def extract_articles(self):
#         df = pd.read_excel(self.input_file)
#         for index, row in df.iterrows():
#             url_id = row['URL_ID']
#             url = row['URL']
#             print(f"Extracting URL_ID: {url_id} from {url}")
#             article_text = self.extract_text(url)
#             if article_text:
#                 output_path = os.path.join(self.output_folder, f"{url_id}.txt")
#                 with open(output_path, 'w', encoding='utf-8') as file:
#                     file.write(article_text)
#             else:
#                 print(f"No content extracted from {url}")
    
#     def __del__(self):
#         self.driver.quit()  # Close the browser when done

# if __name__ == "__main__":
#     input_file = 'input.xlsx'  # Change this to your actual input file path
#     data_extraction = DataExtraction(input_file)
#     data_extraction.extract_articles()

import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Define paths
input_excel_path = 'input.xlsx'
extracted_folder_path = 'Artifact\DataExtraction'
cleaned_folder_path = 'Artifact\DataClean'
output_excel_path = 'output.xlsx'

# Ensure directories exist
os.makedirs(extracted_folder_path, exist_ok=True)
os.makedirs(cleaned_folder_path, exist_ok=True)

# Function to extract content from URL
def extract_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    return ""

# Function to clean extracted text
def clean_text(text):
    # Define your text cleaning logic here
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Function to analyze cleaned text
def analyze_text(text):
    # Define your analysis logic here
    positive_score = text.count("good")  # Example logic
    negative_score = text.count("bad")   # Example logic
    return positive_score, negative_score

# Step 1: Data Extraction
print("Starting data extraction...")
df = pd.read_excel(input_excel_path)
for _, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    content = extract_content(url)
    output_file_path = os.path.join(extracted_folder_path, f"{url_id}.txt")
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)
print("Data extraction completed.")

# Step 2: Text Cleaning
print("Starting text cleaning...")
for file_name in os.listdir(extracted_folder_path):
    input_file_path = os.path.join(extracted_folder_path, file_name)
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    cleaned_content = clean_text(content)
    output_file_path = os.path.join(cleaned_folder_path, file_name)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)
print("Text cleaning completed.")

# Step 3: Analysis
print("Starting analysis...")
data = []
for file_name in os.listdir(cleaned_folder_path):
    input_file_path = os.path.join(cleaned_folder_path, file_name)
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    positive_score, negative_score = analyze_text(content)
    data.append({'URL_ID': file_name.split('.')[0], 'Positive_Score': positive_score, 'Negative_Score': negative_score})
df = pd.DataFrame(data)
df.to_excel(output_excel_path, index=False)
print(f"Analysis completed. Output file saved at {output_excel_path}")
