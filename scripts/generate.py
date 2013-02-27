from jinja2 import Template
import json

with open("sprites.html", 'w') as f:
    template = Template(open('templates/sprites.html').read())
    f.write(template.render(sprites=json.load(open('data/sprites.json'))))

with open("items.html", 'w') as f:
    template = Template(open('templates/items.html').read())
    f.write(template.render(sprites=json.load(open('data/items.json'))))
