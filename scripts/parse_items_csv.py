import csv
import urllib
import os
import json
import string

valid_chars = "-%s%s" % (string.ascii_letters, string.digits)

def slugify(name):
    return ''.join(c for c in name.replace(" ", "-") if c in valid_chars)


with open('csv/Hawkthorne Community To-Do List - Item sprites.csv', 'rb') as csvfile:
    items = []

    for row in csv.reader(csvfile):
        imgur = row[5]

        if len(imgur) == 0 or "imgur" not in imgur:
            print "Skipping " + row[0]
            continue
        
        image = os.path.join("images", "items", slugify(row[0]) + ".png")

        if not os.path.exists(image):
            urllib.urlretrieve(imgur, image)

        items.append({
            'name': row[0],
            'category': row[1],
            'screenshot': row[2],
            'artist': row[3],
            'url': "/" + image
        })

    json.dump(items, open('data/items.json', 'w'))
