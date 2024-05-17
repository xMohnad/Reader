from .PyProbe.PyParse import pyparse 
from bs4 import BeautifulSoup
from .seve_data.tojson import create_or_load_json, conductor

# https://lekmanga.net/manga/
def mangalek(url, json_file):
    manga_data = create_or_load_json(json_file)
    if url in manga_data:
        if manga_data[url]['next_chapter'] is not None and manga_data[url]['next_chapter']:
            return manga_data[url]['image_urls'], manga_data[url]['title'], manga_data[url]['next_chapter'], manga_data[url]['prev_chapter']
    
    soup = pyparse(url)
    main_div = soup.find("div", class_="container")
    
    img_tags = main_div.find_all("img", class_="wp-manga-chapter-img")
      
    image_urls = [img["src"] for img in img_tags]
    title= main_div.find('h1', id='chapter-heading').text.strip()
    
    next_chapter_link = main_div.find('a', class_='next_page')
    next_chapter_link = next_chapter_link['href'] if next_chapter_link else None
    if next_chapter_link is None:
        print("Next chapter link is not available")
        
    prev_chapter_link = main_div.find('a', class_='prev_page')
    prev_chapter_link = prev_chapter_link['href'] if prev_chapter_link else None
    if prev_chapter_link is None:
        print("previous chapter link is not available")
   
    conductor(manga_data, url, image_urls, title, next_chapter_link, prev_chapter_link, json_file)
    return image_urls, title, next_chapter_link, prev_chapter_link