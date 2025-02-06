# Sentiment Analysis Project

# Import necessary libraries
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Data Loading and Preprocessing Class
class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        data = pd.read_csv(self.file_path)
        return data

    def preprocess_data(self):
        data = self.load_data()
        data['processed_text'] = data['review_text'].apply(self.clean_text)
        return data

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\d+', '', text)
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]
        cleaned_text = ' '.join(tokens)
        return cleaned_text

# Sentiment Analysis Class
class SentimentAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def analyze_textblob(self, text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    def analyze_nltk(self, text):
        scores = self.sia.polarity_scores(text)
        return scores['compound']

# Visualization Class
class Visualizer:
    def plot_sentiment_distribution(self, data, column, title):
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column], kde=True)
        plt.title(title)
        plt.xlabel('Sentiment Score')
        plt.ylabel('Frequency')
        plt.show()

    def plot_comparison(self, data, title):
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x='textblob_sentiment', y='nltk_sentiment', data=data)
        plt.title(title)
        plt.xlabel('TextBlob Sentiment')
        plt.ylabel('NLTK Sentiment')
        plt.show()

# Function to calculate agreement between TextBlob and NLTK
def calculate_agreement(data):
    # ... (implementation for agreement calculation) ...
    # Placeholder for demonstration
    agreement = 0.75  # Example value
    return agreement

# Function to display sample data
def sample_data(data, n=5):
    return data.sample(n)

# Main function
def main():
    # Create a sample dataset (replace this with your own data loading logic)
    reviews_df = pd.DataFrame({
        'review_text': [
            "I love this product! It's amazing and works perfectly.",
            "This is the worst purchase I've ever made. Terrible quality.",
            "The product is okay, but not great. It could be better.",
            "Absolutely fantastic! Exceeded all my expectations.",
            "I'm very disappointed with this item. Don't buy it.",
            "It's alright, does the job but nothing special.",
            "Great value for money, highly recommended!",
            "Poor customer service and the product broke after a week.",
            "Not bad, but also not particularly impressive.",
            "This is exactly what I was looking for. Perfect!"
        ]
    })

    # Save the sample data to a CSV file
    reviews_df.to_csv('sample_reviews.csv', index=False)

    # Load and preprocess data
    loader = DataLoader('sample_reviews.csv')
    data = loader.load_data()
    processed_data = loader.preprocess_data()

    # Perform sentiment analysis
    analyzer = SentimentAnalyzer()
    processed_data['textblob_sentiment'] = processed_data['processed_text'].apply(analyzer.analyze_textblob)
    processed_data['nltk_sentiment'] = processed_data['processed_text'].apply(analyzer.analyze_nltk)

    # Visualize results
    visualizer = Visualizer()
    visualizer.plot_sentiment_distribution(processed_data, 'textblob_sentiment', 'TextBlob Sentiment Distribution')
    visualizer.plot_sentiment_distribution(processed_data, 'nltk_sentiment', 'NLTK Sentiment Distribution')
    visualizer.plot_comparison(processed_data, 'Sentiment Analysis Comparison')

    # Print sample results and agreement
    print("\nSample results:")
    print(sample_data(processed_data[['review_text', 'textblob_sentiment', 'nltk_sentiment']], n=5))

    agreement = calculate_agreement(processed_data)
    print(f"\nAgreement between TextBlob and NLTK: {agreement:.2f}%")

# Run the main function
if __name__ == "__main__":
    main()