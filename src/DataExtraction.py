
import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from src.constant import CHROME_DRIVER_PATH


class DataExtraction:
    def __init__(self, input_file, output_folder="Artifact/DataExtraction"):
        self.input_file = input_file
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)
        
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)
    
    def extract_text(self, url):
        try:
            self.driver.get(url)
            time.sleep(2)
            
            header = self.driver.find_element(By.XPATH, '//h1[@class="entry-title"]').text
            content = self.driver.find_element(By.CLASS_NAME, 'td-post-content.tagdiv-type').text
            
            return header + '\n' + content
        except (NoSuchElementException, WebDriverException) as e:
            print(f"Failed to extract {url}: {e}")
            return ""
    
    def extract_articles(self):
        df = pd.read_excel(self.input_file)
        for index, row in df.iterrows():
            url_id = row['URL_ID']
            url = row['URL']
            print(f"Extracting URL_ID: {url_id} from {url}")
            article_text = self.extract_text(url)
            if article_text:
                output_path = os.path.join(self.output_folder, f"{url_id}.txt")
                with open(output_path, 'w', encoding='utf-8') as file:
                    file.write(article_text)
            else:
                print(f"No content extracted from {url}")
    
    def __del__(self):
        self.driver.quit()

