import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException

class DataExtraction:
    def __init__(self, input_file, output_folder="Artifact\DataExtraction"):
        self.input_file = input_file
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)
        
        # Initialize the Selenium WebDriver
        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
        # Set path to the ChromeDriver executable
        chrome_driver_path = 'chromedriver.exe'  # Update this path
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    def extract_text(self, url):
        try:
            self.driver.get(url)
            time.sleep(2)  # Wait for the page to load
            
            #header = self.driver.find_element(By.CLASS_NAME, 'entry-title').text
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
        self.driver.quit()  # Close the browser when done

if __name__ == "__main__":
    input_file = 'input.xlsx'  # Change this to your actual input file path
    data_extraction = DataExtraction(input_file)
    data_extraction.extract_articles()

