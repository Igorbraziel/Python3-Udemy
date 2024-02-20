import os
import json

file_name = "JSON_files.json"

#absolute_path_file = os.path.join(os.path.abspath('.'), file_name)

absolute_path_file = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        file_name
    )
)

movie = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',     
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring', 
    'is_movie': True, 
    'imdb_rating': 8.8, 
    'year': 2001, 
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'], 
    'budget': None
    }

with open(absolute_path_file, 'w') as file_:
    json.dump(movie, file_, indent=2, ensure_ascii=False)
    
with open(absolute_path_file, 'r') as json_file:
    movie_from_json = json.load(json_file)
    print(movie_from_json)


