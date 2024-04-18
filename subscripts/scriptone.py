import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import torch
from transformers import BertTokenizer, BertModel
import numpy as np
import networkx as nx

nltk.download('punkt')
nltk.download('stopwords')

def read_book(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def preprocess_text(text):
    sentences = sent_tokenize(text)
    clean_sentences = [sentence.lower() for sentence in sentences if sentence.strip() != '']
    return clean_sentences

def sentence_embedding(sent, model, tokenizer):
    inputs = tokenizer(sent, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

def build_similarity_matrix(embeddings):
    similarity_matrix = np.zeros((len(embeddings), len(embeddings)))
    for i in range(len(embeddings)):
        for j in range(len(embeddings)):
            similarity_matrix[i][j] = np.dot(embeddings[i], embeddings[j]) / (np.linalg.norm(embeddings[i]) * np.linalg.norm(embeddings[j]))
    return similarity_matrix

def generate_summary(book_path, num_sentences=5):
    text = read_book(book_path)
    sentences = preprocess_text(text)
    
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    
    embeddings = [sentence_embedding(sent, model, tokenizer) for sent in sentences]
    similarity_matrix = build_similarity_matrix(embeddings)
    
    sentence_similarity_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    summary = ''
    for i in range(min(num_sentences, len(ranked_sentences))):
        summary += ranked_sentences[i][1] + " "
    return summary

# Example usage:
book_path = 'book.txt'
summary = generate_summary(book_path, num_sentences=2)
print(summary)
