import os
import json 

def create_or_load_json(json_file):
    if os.path.exists(json_file):
        with open(json_file, 'r') as file:
            return json.load(file)
            
    else:
        return {}

def save_to_json(data, json_file):
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)
        
def conductor(manga_data, url, image_urls, title, next_chapter_link, prev_chapter_link, json_file):
    manga_data[url] = {
        'image_urls': image_urls,
        'title': title,
        'next_chapter': next_chapter_link,
        'prev_chapter': prev_chapter_link
    }
    save_to_json(manga_data, json_file)
