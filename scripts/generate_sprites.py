from jinja2 import Template
import json

template = Template(open('templates/sprites.html').read())

print template.render(sprites=json.load(open('data/sprites.json')))
