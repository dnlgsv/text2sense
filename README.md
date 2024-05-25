# text2sense

**text2sense** is a comprehensive tool designed to analyze and enhance text-based content using a variety of advanced techniques, including Natural Language Processing (NLP), Large Language Models (LLM), Computer Vision, Audio Processing, and Recommendation Systems. 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The idea behind **text2sense** is to take a book file, article, or simple text transcription of a video, and process it to provide valuable insights and functionalities. This tool can estimate the author's vocabulary size, identify frequent words and phrases, generate summaries, and even recommend similar books based on unique attributes like plot, style, and vocabulary.

## Features

### Functionalities Based on Python Scripts and Classical NLP Approaches
1. **Vocabulary Size Estimation**: ![status](https://img.shields.io/badge/status-planned-lightgrey)

Estimate the author's vocabulary size based on the text.

2. **Frequent Words and Phrases**: ![status](https://img.shields.io/badge/status-done-brightgreen) 

Identify the most frequent unigrams, bigrams, trigrams, etc.

3. **Useful Words**: ![status](https://img.shields.io/badge/status-in%20progress-yellow)

Find the overlap between the most frequent words in the text and the language.

4. **Archaic Words**: ![status](https://img.shields.io/badge/status-planned-lightgrey)

Detect archaic words useful for language learners.

5. **Genre Prediction**: ![status](https://img.shields.io/badge/status-planned-lightgrey)

Predict the genre of the text.

6. **Title Generation**: ![status](https://img.shields.io/badge/status-planned-lightgrey)

Generate a title for the text.

7. **Anki Dictionary Generation**: ![status](https://img.shields.io/badge/status-planned-lightgrey)

Create an Anki dictionary from the text for language learning.

### Functionalities Based on LLM
8. **Text Summarization**: ![status](https://img.shields.io/badge/status-planned-lightgrey)

Generate a brief summary of the text.

9. **Question-Answering**: ![status](https://img.shields.io/badge/status-planned-lightgrey)

Answer questions based on the text's content.

10. **New Text Generation**: ![status](https://img.shields.io/badge/status-planned-lightgrey)

Generate new text in the author's style.

11. **Fanfic Crossover**: ![status](https://img.shields.io/badge/status-planned-lightgrey)

Create crossover fanfiction based on multiple books.

### Functionalities Based on Computer Vision
12. **Illustration Generation**: ![status](https://img.shields.io/badge/status-planned-lightgrey)

Generate illustrations based on the text's main ideas.

13. **Character Portraits**: ![status](https://img.shields.io/badge/status-planned-lightgrey)

Create portraits of the characters.

### Functionalities Based on Audio Processing
14. **Audio Recording**: ![status](https://img.shields.io/badge/status-planned-lightgrey)

Provide an audio recording of the text.

### Functionalities Based on Recommendation Systems
15. **Similar Content Recommendation**: ![status](https://img.shields.io/badge/status-planned-lightgrey)

Recommend similar books, articles, and videos based on plot, style, and vocabulary.

## Installation

To install **text2sense**, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/text2sense.git
cd text2sense
pip install -r requirements.txt
```

## Usage

Upload a Text: Upload a book file, article, or text transcription of a video.
Run Analysis: Use the built-in models and scripts to analyze the text and generate insights.
View Results: Access the results, including vocabulary estimation, frequent phrases, text summaries, and more.

```bash
from text2sense import analyze_text

results = analyze_text('path_to_text_file.txt')
print(results)
```

## License

Not defined yet.

## Contact

For any questions or feedback, please contact me.