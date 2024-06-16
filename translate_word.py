import requests
from deco_1 import logger

url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = 'dict.1.1.20220928T183617Z.4449b33063fe4328.b93679d48620ed6f3c20da6bff0237bcbd0e8d6a'


@logger
def translate_word(word):
    trans_word_json = requests.get(url+f'?key={token}&lang=ru-en&text={word}').json()
    trans_word = trans_word_json['def'][0]['tr'][0]['text']
    return trans_word