# Файл в котором я попытаюсь создать функцию по поиску слов в тексте
from test_text import test_text

def find_string_by_word(strings, word):

    for string in strings:
        if word.lower() in string.lower():
            return string
    return None


word = "алгебра"
test_text = test_text.split('.')




if __name__ == "__main__":
    result = find_string_by_word(test_text, word)

    if result:
        print(f"Искомое слово '{word}' найдено в строке: {result}")
    else:
        print(f"Искомое слово '{word}' не найдено.")


