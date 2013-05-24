from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(open('sprites.html'))

sprites = soup.find('ul', class_="sprites")

output = []

for sprite in sprites.find_all('li'):
    name, artist = sprite.find_all('p')

    original = None
        
    if name.find('a') is not None:
        original = name.find('a')['href']

    if sprite.find('img') is None:
        print sprite
        continue

    output.append({
        'sprite_url': sprite.find('img')['src'],
        'original_url': original,
        'name': name.string,
        'artist': artist.find('a').text,
    })

json.dump(output, open('data/sprites.json', 'w'))
