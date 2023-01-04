.PHONY: init translate

translate:
	python scripts/translate_terrain.py japanese/terrain.txt

init:
	pip install -r requirements.txt

