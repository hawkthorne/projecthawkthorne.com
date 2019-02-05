.PHONY: pages

pages: index.md sprites.html

items.html: data/items.json venv
	sh -c ". venv/bin/activate; python scripts/generate.py"

sprites.html: data/sprites.json venv
	sh -c ". venv/bin/activate; python scripts/generate.py"

venv:
	virtualenv venv
	sh -c ". venv/bin/activate; pip install -r requirements.txt"
