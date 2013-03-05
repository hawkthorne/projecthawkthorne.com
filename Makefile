.PHONY: pages

pages: index.html sprites.html

items.html: data/items.json venv
	. venv/bin/activate; python scripts/generate.py

sprites.html: data/sprites.json venv
	. venv/bin/activate; python scripts/generate.py

venv:
	virtualenv venv
	. venv/bin/activate; pip install -r requirements.txt
