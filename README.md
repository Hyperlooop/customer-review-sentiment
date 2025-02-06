# Sentiment Analysis Using NLP

## 📌 Project Overview
This project is a **Sentiment Analysis Tool** that processes customer reviews using **Natural Language Processing (NLP)** techniques. It classifies text into **positive, negative, or neutral sentiment** using **TextBlob and NLTK Vader**, then visualizes the results with **Matplotlib and Seaborn**.

## 🔍 Features
✅ **Data Cleaning & Preprocessing** (removes stopwords, punctuation, and tokenizes text)
✅ **Sentiment Classification** using **TextBlob** & **NLTK Vader**
✅ **Visualization of Sentiment Scores** using **Matplotlib & Seaborn**
✅ **Automated CSV Processing** with **Pandas**
✅ **Comparing Sentiment Scores** between two different NLP models

## 🛠️ Tech Stack
- **Programming Language:** Python 🐍
- **Libraries:** Pandas, NLTK, TextBlob, Matplotlib, Seaborn
- **NLP Tools:** Tokenization, Stopword Removal, Vader Sentiment Analyzer

## 📂 Project Structure
```
📁 sentiment-analysis-nlp
│── data/                # Sample dataset (CSV file)
│── src/                 # Source code
│   ├── data_loader.py   # Handles data loading and preprocessing
│   ├── sentiment_analyzer.py  # Performs sentiment analysis
│   ├── visualizer.py    # Generates sentiment visualizations
│   ├── main.py          # Main script to run the analysis
│── README.md            # Project documentation
```

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/sentiment-analysis-nlp.git
cd sentiment-analysis-nlp
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Project
```sh
python main.py
```

## 📊 Sample Output
Here’s what the sentiment analysis results look like:
```
Sample results:
-------------------------------------
Review: "I love this product! It's amazing."
TextBlob Sentiment: 0.85 (Positive)
NLTK Sentiment: 0.91 (Positive)
-------------------------------------
Review: "Worst purchase ever. Waste of money."
TextBlob Sentiment: -0.75 (Negative)
NLTK Sentiment: -0.83 (Negative)
```

## 🎨 Visualizations
The project generates **histograms** and **scatter plots** to show sentiment distribution.
![Sentiment Distribution](https://via.placeholder.com/500x300)

## 🤝 Contributions
Want to improve this project? Feel free to **fork the repo**, make changes, and submit a **pull request**!

## 📜 License
This project is open-source under the **MIT License**. 

---
🚀 **Happy Coding!** 🎉

