import deepl
import os
import pyperclip

API_KEY = os.environ["DEEPL_API_KEY"]

translated_cache = {}

translator = deepl.Translator(API_KEY)

def translate(text):
	if text in translated_cache:
		return translated_cache[text]
	output = translator.translate_text(text, target_lang = "JA")
	translated_cache[text] = output.text
	return output.text

