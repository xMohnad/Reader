from .PyProbe.PyParse import pyparse 
from bs4 import BeautifulSoup
import re
from .seve_data.tojson import create_or_load_json, conductor

# https://www.teamxnovel.com/series/BATE/1
def get_title(url):
    url_home = re.match(r'(https?://[^/]+/[^/]+/[^/]+)/\d+(\.\d+)?', url).group(1)
    soup = pyparse(url_home)
    mangnama = soup.find('div', class_='author-info-title').find('h6').text.strip()
    chapter_number = re.search(r'(?<=\/)\d+(\.\d+)?', url).group()
    title = f"{mangnama} {chapter_number}"
    return title
    
def teamx(url, json_file):
    
    manga_data = create_or_load_json(json_file)
    if url in manga_data:
        return manga_data[url]['image_urls'], manga_data[url]['title'], manga_data[url]['next_chapter'], manga_data[url]['prev_chapter']
        
    soup = pyparse(url)
    reader_area = soup.find_all('div', class_="page-break")
    
    if reader_area:
        image_urls = [img.get("src") for div in reader_area for img in div.find_all("img") if img.get("src")]
    else:
        print("Images not found.")
    title = get_title(url)
    
    nextprev_link = soup.find('div', class_="container")
    next_chapter_link = nextprev_link.find('a', id='next-chapter')
    next_chapter_link = next_chapter_link['href']
    if next_chapter_link == "#":
        print("Next chapter link is not available")
        next_chapter_link = None
    prev_chapter_link = nextprev_link.find('a', id='prev-chapter')
    prev_chapter_link = prev_chapter_link['href']
    if prev_chapter_link == '#':
        prev_chapter_link = None
        print("previous chapter link is not available")
        
    conductor(manga_data, url, image_urls, title, next_chapter_link, prev_chapter_link, json_file )
    return image_urls, title, next_chapter_link, prev_chapter_link
