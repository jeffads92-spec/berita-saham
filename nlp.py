import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize Sentiment Intensity Analyzer
nltk.download('vader_lexicon')
sentiment_analyzer = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis

def analyze_sentiment(text):
    scores = sentiment_analyzer.polarity_scores(text)
    return scores

# Function for keyword extraction

def extract_keywords(text, num_keywords=5):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    dense = tfidf_matrix.todense()
    denselist = dense.tolist()
    df_tfidf = pd.DataFrame(denselist, columns=feature_names)
    keywords = df_tfidf.T.sort_values(by=0, ascending=False)
    return keywords.head(num_keywords).index.tolist()

# Example usage
if __name__ == '__main__':
    sample_text = "I love programming in Python!"
    print(analyze_sentiment(sample_text))
    print(extract_keywords(sample_text))