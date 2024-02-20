import json
from pprint import pprint
string_json = """
{
    "title" : "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
"""
filme = json.loads(string_json)
print(json.dumps(filme, ensure_ascii = False, indent = 2))