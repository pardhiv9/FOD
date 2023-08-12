import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load the dataset from CSV file
def load_dataset(file_path, column_name):
    data = pd.read_csv(file_path)
    return data[column_name]

# Preprocess text data
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in punctuation and word not in stop_words]
    return tokens

# Display top N most frequent words and their frequencies
def display_top_words(word_counts, n):
    top_words = word_counts.most_common(n)
    print(f"Top {n} most frequent words:")
    for word, frequency in top_words:
        print(f"{word}: {frequency}")

# Plot a bar graph to visualize top N most frequent words
def plot_word_frequency(word_counts, n):
    top_words, top_frequencies = zip(*word_counts.most_common(n))
    plt.figure(figsize=(10, 6))
    plt.bar(top_words, top_frequencies)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title(f"Top {n} Most Frequent Words")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main program
if __name__ == "__main__":
    file_path = "data.csv"  # Replace with the actual file path
    column_name = "feedback"
    N = int(input("Enter the number of top words to display: "))

    # Load NLTK resources
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    punctuation = set(string.punctuation)
    stop_words = set(stopwords.words("english"))

    # Load the dataset
    feedback_data = load_dataset(file_path, column_name)

    # Preprocess and calculate word frequencies
    all_words = []
    for feedback in feedback_data:
        tokens = preprocess_text(feedback)
        all_words.extend(tokens)
    word_counts = Counter(all_words)

    # Display top words and frequencies
    display_top_words(word_counts, N)

    # Plot word frequency distribution
    plot_word_frequency(word_counts, N)
