# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:53:59 2020

@author: Agnieszka
"""
import nltk
from nltk.tokenize import word_tokenize
import string

class Document:
    def __init__(self):
        self.text = ""
        self.freq_dict = {}

    def load_file(self, path):
        with open(path) as file:
            self.text = file.read()

    def close_file(self):
        self.text = ""
        self.freq_dict = {}

    def remove_punctuation(self):
        text = ""
        for element in self.text:
            if element not in string.punctuation:
                if element != "I":
                    text += element.lower()
                else:
                    text +=element
        return text

    def get_frequencies(self): 
        if len(self.freq_dict) != 0:
            return self.freq_dict
        text = self.remove_punctuation().split()
        for word in text:
            word = word.lower()
            if word not in self.freq_dict:
                self.freq_dict[word] = 0
            self.freq_dict[word] += 1

    def annotate(self):
        tokenized = word_tokenize(self.remove_punctuation())
        return nltk.pos_tag(tokenized, tagset='universal')

    def count_unique(self):
        if len(self.freq_dict) == 0:
            self.get_frequencies()
        return len(self.freq_dict)

    def count_tokens(self):
        return len(self.remove_punctuation().split())

    def type2token_ratio(self):
        return round(self.count_unique() / self.count_tokens(), 3)
    
    def pos (self, pos_tag):
        annotated = self.annotate()
        unique = set()
        counter = 0
        for word, pos_id in annotated:
            if pos_id.startswith(pos_tag):
                counter += 1
                unique.add(word)
        pairs = []
        freq_dict = self.get_frequencies()
        for word in unique:
            pair = (word, freq_dict[word.lower()])
            pairs.append(pair)
        sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
        return counter, sorted_pairs

    
    