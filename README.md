# text_extractor

# Objective
The objective of this project is to extract textual data from articles given in a URL and perform text analysis to compute several variables, including sentiment scores, readability, passive words, and personal pronouns.

## Solution:

We are extracting article text from URLs listed in Input.xlsx using Selenium in DataExtraction.py then storing it in Artifact\DataExtraction folder with respect to there URL_ID, cleaned the text by removing stopwords in TextCleaning.py and store in Artifact\CleanDat folder, and analyzed the text for various metrics (sentiment, readability, etc.) in TextAnalysis.py. Finally, we are combining these analysis results with the original input data and saved everything in the structured format in Output Data Structure.xlsx.

### Data Extraction
Input File: input.xlsx
Task: For each URL provided in input.xlsx, we are extracted the article text and saved it in a text file named with the URL_ID. also ensured that only the article title and article text were extracted, excluding headers, footers, or any other non-article content.
Tools Used: Python programming with libraries such as BeautifulSoup, Selenium, Scrapy, etc.
Data Analysis

### Data Cleaning
The TextCleaning class initializes with a set of English stopwords using NLTK. The clean_text method tokenizes the input text, filters out non-alphabetic tokens (except periods) and stopwords, and then rejoins the cleaned words into a single string. This process ensures the text is prepped for further analysis by removing common, insignificant words

### Sentiment Analysis
The SentimentAnalysis class performs sentiment and readability analysis on text. It initializes with sets of positive/negative words, stopwords, and a syllable dictionary. Methods include cleaning text, calculating sentiment scores (positive, negative, polarity, subjectivity), readability metrics (average sentence length, complex words, Fog Index), and other statistics like word count, syllable count per word, and average word length. Additionally, it counts personal pronouns and computes the average number of words per sentence.

```
[Input.xlsx]
      |
      V
[DataExtraction.py]
      |
      |-- (__init__)
      |      |-- Setup WebDriver
      |      |-- Setup Output Directory
      |
      |-- (extract_articles)
      |      |-- Read URLs from Input.xlsx
      |      |-- Call extract_text
      |      |-- Save extracted articles (URL_ID.txt)
      |
      |-- (extract_text)
             |-- Extract title and article text
             |-- Handle exceptions
             |-- Ensure only article content is extracted
      |
      V
[Extracted Articles (URL_ID.txt)]
      |
      V
[TextCleaning.py]
      |
      |-- (__init__)
      |      |-- Setup Stopwords
      |
      |-- (clean_text)
             |-- Tokenize text
             |-- Remove stopwords
             |-- Join cleaned text
      |
      V
[Cleaned Articles]
      |
      V
[TextAnalysis.py]
      |
      |-- (__init__)
      |      |-- Setup variables and resources
      |
      |-- (analyze_text)
             |-- Read cleaned text
             |-- Compute text analysis metrics
             |-- Save analysis results
      |
      V
[Output Data Structure.xlsx]
      |
      V
[Final Output]
      |-- Combine input variables with analysis results
      |-- Save to Output Data Structure.xlsx

```

## How to Eun project 
### Step 1-: Clone the Repository
```bash
git clone 
```

### Step 2-: Creat conda environment
```bash
conda create -p ./venv python=3.10 -y
```

### Step 3-: Activate Conda environment
```bash
conda activate venv/
```

### Step 4-: Install requirements
```bash
pip install -r requirements.txt
```

### step 5 -: Run file
```bash
python main.py
```
