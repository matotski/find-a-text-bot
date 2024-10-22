# Файл в котором я попытаюсь создать функцию по поиску слов в файлах
import re
from codecs import ignore_errors

from nltk.tokenize import sent_tokenize

def file_reader(file_path, search_word):



    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()

    sentences = sent_tokenize(text)
    matching_sentences = [sentence for sentence in sentences if re.search(r'\b' + search_word + r'\b', sentence, re.IGNORECASE)]

    return matching_sentences

sentences = file_reader('test_text.txt', '')


