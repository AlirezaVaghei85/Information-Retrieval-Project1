<div align="center">

# 🔍 BST-Based Information Retrieval System

**A Python implementation of an Inverted Index using Binary Search Trees for the Reuters Corpus.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![NLTK](https://img.shields.io/badge/NLTK-Corpus-green.svg)](https://www.nltk.org/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

</div>

---

## 📌 Overview

This project is a custom **Information Retrieval (IR) System** built from scratch in Python. It constructs an **Inverted Index** using a **Binary Search Tree (BST)** data structure to index and search documents from the famous **NLTK Reuters Dataset**.

The system supports single-term search, boolean `AND` queries using document ID intersection, memory consumption monitoring, and term frequency analysis.

---

## ✨ Features

* 🌳 **BST Inverted Index:** Efficient lookup, insertion, and traversal using dynamic Binary Search Trees.
* 📚 **Reuters Corpus Integration:** Tokenization and preprocessing of real-world text dataset documents.
* 🔎 **Single-Term Search:** Quick retrieval of document IDs containing a specific keyword.
* ⚡ **Boolean Query Processing (`AND` Operator):** Fast set intersection algorithm to evaluate queries like `term1 AND term2`.
* 📊 **Frequency Analysis:** Capability to traverse the BST and extract the top 30 most frequent terms across the dataset.
* ⚙️ **Resource Monitoring:** Real-time RAM usage tracking using `psutil`.

---

## 🛠️ Data Structure & Architecture

Each node in the Binary Search Tree stores a **term** and a sorted list of **DocIDs** (Posting List) where the term appears:

```text
               [ Node: "market" ]
               /                \
     [ Node: "apple" ]    [ Node: "oil" ]
      DocIDs: [1, 5, 9]    DocIDs: [2, 4, 10]
```

### Boolean Query Optimization
For boolean `AND` queries, the system performs a synchronized two-pointer merge traversal over the sorted posting lists of both terms, yielding an $O(N + M)$ time complexity where $N$ and $M$ are the posting list lengths.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed along with the required libraries:

```bash
pip install nltk psutil
```

### Dataset Preparation

If you don't have `data.pkl` generated yet, uncomment the dataset downloading snippet in the main script to process and dump the Reuters corpus:

```python
import nltk
from nltk.corpus import reuters
from nltk.tokenize import word_tokenize

nltk.download('reuters')
nltk.download('punkt')

# Preprocessing & Pickling logic...
```

---

## 💻 Usage

Run the main Python script:

```bash
python main.py
```

Upon launching, the system displays current memory consumption and presents an interactive command-line interface:

```text
Memory usage: 142.15 MB

1. Search for one query
2. Search for two queries with AND
3. See 30 most frequent terms
Choose an option: 
```

### Options

1. **Single Term Search:**
   * Enter a single word (e.g., `oil`).
   * Output: Total document count and the first 10 Document IDs.

2. **Boolean Search (`AND`):**
   * Enter a two-term expression formatted as `term1 AND term2` (e.g., `oil AND market`).
   * Output: Intersected document list containing both terms.

3. **Top Frequent Terms:**
   * Ranks and prints the 30 most frequent terms in the inverted index.

---

## 📝 Example Output

```text
Choose an option: 2
Enter your query: oil AND market
Query: ['oil', 'AND', 'market']
Documents retrieved: 142
Doc IDs: ['reuters-10012', 'reuters-10082', 'reuters-10110', ...]
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
