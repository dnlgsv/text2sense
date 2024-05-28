import re
import argparse
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK data (stopwords and punkt tokenizer)
nltk.download('stopwords')
nltk.download('punkt')

def read_file(file_path, encoding='utf-8'):
    """
    Read the contents of a file and return it as a string.
    
    Args:
        file_path (str): The path to the file.
        encoding (str, optional): The file encoding (default: utf-8).
    
    Returns:
        str: The contents of the file.
    """
    
    try:
        with open(file_path, 'r', encoding=encoding) as file_obj:
            return file_obj.read()
    except Exception as error:
        print('Error reading file: ' + str(error))
        return None

def process_text(text, remove_stopwords=True):
    """
    Process the given text by converting it to lowercase, removing non-alphanumeric characters,
    tokenizing it into words, and optionally removing stopwords.
    
    Args:
        text (str): The text to process.
        remove_stopwords (bool, optional): Whether to remove stopwords. Defaults to True.
    
    Returns:
        list: The processed words.
    """
    
    # Convert text to lowercase
    text = text.lower()
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Tokenize text into words
    words = word_tokenize(text)
    # Remove stopwords
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words]
    return words

def find_most_frequent_words(words, top_n=10):
    word_counts = Counter(words)
    return word_counts.most_common(top_n)

def plot_word_frequency(word_freq):
    words, frequencies = zip(*word_freq)
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top Most Frequent Words')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find and display the most frequent words in a text file.")
    parser.add_argument('file_path', type=str, help="Path to the text file.")
    parser.add_argument('--encoding', type=str, default='utf-8', help="File encoding (default: utf-8).")
    parser.add_argument('--top_n', type=int, default=10, help="Number of most frequent words to display (default: 10).")
    parser.add_argument('--no_stopwords', action='store_true', help="Exclude common stopwords.")
    
    args = parser.parse_args()
    
    text = read_file(args.file_path, args.encoding)
    if text:
        words = process_text(text, not args.no_stopwords)
        most_frequent_words = find_most_frequent_words(words, args.top_n)
        
        print("Most Frequent Words:")
        for word, freq in most_frequent_words:
            print(f"{word}: {freq}")
        
        plot_word_frequency(most_frequent_words)
