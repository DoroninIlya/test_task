import argparse
import re

PATTERN = '([^a-zA-Zа-яА-Я](\\s)?|\\s+)+'
DESCRIPTION = 'Подсчет частоты встречаемости слова в файле'
FILE_HELP = (
    'Имя и/или путь до файла, в котором нужно произвести подсчет ' +
    'частоты встречаемости'
    )
WORD_HELP = 'Слово, частоту встречаемости которого нужно найти'

parser = argparse.ArgumentParser(description=DESCRIPTION)

parser.add_argument('-f', dest='file_name', required=True, help=FILE_HELP)
parser.add_argument('-w', dest='word', required=True, help=WORD_HELP)

arguments = parser.parse_args()

file_name = arguments.file_name
word_for_search = arguments.word.lower()

file_content = ''
count_of_word = 0

with open(file_name, encoding='UTF-8') as file:
    file_content = file.read()

punctuationless_file_content = re.sub(PATTERN, ' ', file_content)

file_words = punctuationless_file_content.split(' ')

for word in file_words:
    if word.lower() == word_for_search:
        count_of_word = count_of_word + 1

print(f'Частота встречаемости слова "{word_for_search}" в файле "{file_name}": {count_of_word}')
