from .PyProbe.PyParse import pyparse 
from bs4 import BeautifulSoup
from .seve_data.tojson import create_or_load_json, conductor

# https://mangapro.club/
def manga_pro(url, json_file):

    manga_data = create_or_load_json(json_file)
    if url in manga_data:
        if manga_data[url]['next_chapter'] is not None and manga_data[url]['next_chapter']:
            print("True")
            return manga_data[url]['image_urls'], manga_data[url]['title'], manga_data[url]['next_chapter'], manga_data[url]['prev_chapter']

    image_urls = []
    soup = pyparse(url)
    reader_area = soup.find('div', id="readerarea")
    title = soup.find('h1', class_='entry-title').text.strip()
    if reader_area:
        image_urls.extend([img['src'] for img in reader_area.find_all('img')])
    else:
        print("Images not found.")
        
    nextprev_link = soup.find('div', class_="nextprev")
    
    next_chapter_link = nextprev_link.find('a', rel='next')

    if next_chapter_link and next_chapter_link['href'] != "https://mangapro.club//":
        next_chapter_link = next_chapter_link['href']
    else:
        next_chapter_link = None
        print("Next chapter link is not available")
        
    prev_chapter_link = nextprev_link.find('a', rel='prev')
    prev_chapter_link = prev_chapter_link['href'] if prev_chapter_link else None
    if prev_chapter_link is None:
        print("previous chapter link is not available")
        
    conductor(manga_data, url, image_urls, title, next_chapter_link, prev_chapter_link, json_file)
    return image_urls, title, next_chapter_link, prev_chapter_link