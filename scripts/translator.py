import deepl
import os
import pyperclip

API_KEY = os.environ["DEEPL_API_KEY"]

translated_cache = {}

translator = deepl.Translator(API_KEY)


def translate(text):
    if text in translated_cache:
        print("%s => %s (cached)" % (text, translated_cache[text]))
        return translated_cache[text]
    output = translator.translate_text(text, target_lang="JA")
    translated_cache[text] = output.text
    print("%s => %s" % (text, output.text))
    return output.text
