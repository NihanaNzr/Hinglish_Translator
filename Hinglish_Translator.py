# -*- coding: utf-8 -*-
"""Hinglish_Translator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xQkXOIxkM7TIFDbTGND8iwx2Pm-vGOuD
"""

pip install transformers

from transformers import MarianMTModel, MarianTokenizer

import re

import nltk
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

""" create an instance of the WordNetLemmatizer class from the Natural Language Toolkit (NLTK) library

"""

lemmatizer = WordNetLemmatizer()

"""For text tokenization, Install 'sentencepiece'."""

pip install sentencepiece

"""Load pre-trained model from Huggingface Transformer"""

model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-hi")
tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hi")

"""Function for nouns and verbs"""

def verbs_nouns(eng_statement):
    words = word_tokenize(eng_statement)
    tagged_words = pos_tag(words)
    auxiliary_verbs = ['am', 'is', 'are', 'was', 'were', 'has', 'had']
    nouns = [words for words, pos in tagged_words if pos.startswith('NN')]

    verbs = [word for word, pos in tagged_words if pos.startswith('VB')and word
             not in auxiliary_verbs]

    verbs = [lemmatizer.lemmatize(verb, pos='v') for verb in verbs]

    translated_words = {'feedback':'प्रतिक्रिया', 'definitely':'निश्चित', 'section':'खण्ड'}
    for noun in nouns:
            hi_noun = hi_translation(noun)
            translated_words[noun] = hi_noun
    for verb in verbs:
        hi_verb = hi_translation(verb)
        modified_value = hi_verb.split(' ', 1)[0]
        translated_words[verb] = modified_value
    return translated_words

"""Function to convert Hindi to Hinglish"""

def hi_translation(eng_statement):
    inputs = tokenizer.encode(eng_statement, return_tensors="pt")
    translated_id = model.generate(inputs, max_length=150, num_return_sequences=1, num_beams=4)
    translated_output=tokenizer.decode(translated_id[0], skip_special_tokens=True)
    translated_output = translated_output.replace('\u200d', '') # handle ZWJ characters
    return translated_output

"""Hindi nouns are replaced with English nouns in order to maintain some English words."""

def noun_switch(nouns, hinglish_text):
    for key, value in nouns.items():
        matches = re.findall(r'\b' + re.escape(value) + r'\b', hinglish_text)
        for match in matches:
            hinglish_text = hinglish_text.replace(match, key)
    return hinglish_text

import nltk
nltk.download('punkt')

import nltk
nltk.download('all')

"""Output Function"""

eng_statement = input("INPUT : ")
nouns = verbs_nouns(eng_statement)
hi_text = hi_translation(eng_statement)
for eng_word, hin_word in nouns.items():
    hi_text = hi_text.replace(hin_word, eng_word)

print(hi_text)

eng_statement = input("INPUT : ")
nouns = verbs_nouns(eng_statement)
hi_text = hi_translation(eng_statement)
for eng_word, hin_word in nouns.items():
    hi_text = hi_text.replace(hin_word, eng_word)

print(hi_text)

eng_statement = input("INPUT : ")
nouns = verbs_nouns(eng_statement)
hi_text = hi_translation(eng_statement)
for eng_word, hin_word in nouns.items():
    hi_text = hi_text.replace(hin_word, eng_word)

print(hi_text)
