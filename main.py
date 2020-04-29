import requests

#  Documentation provided from the base file -  https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def machine_translating(source_text, translated_text, source_language, language_to_translate = 'ru'):
    
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-key>
     & text = <a text to be translated>
     & lang = <so-called direction of translation>
     & [format = <a text's format>]
     & [options = <translation options>]
     & [callback = <the name of the callback-function>]
    :param to_lang:
    :return:
    
    """
    
    with open(source_text, 'r') as file_to_process:

        params = {
        'key': API_KEY,
        'text': file_to_process.read(),
        'lang': '{}-{}'.format(source_language, language_to_translate),
        }
    
    response = requests.get(URL, params=params)
    json_ = response.json()
    result = ''.join(json_['text'])

    with open(translated_text, 'w') as file_translated:
        file_translated.write(result)


if __name__ == '__main__':
    
    machine_translating('FR.txt', 'translated_FR.txt', 'fr')
    machine_translating('DE.txt', 'translated_DE.txt', 'de')
    machine_translating('ES.txt', 'translated_ES.txt', 'es')