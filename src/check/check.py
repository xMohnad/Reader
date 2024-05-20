from src.mangapro import manga_pro
from src.Teamx import teamx
from src.Mangalek import mangalek
from src._3asq import _3asq

def checkselection(url):
    if "mangapro" in url:
        json_file = "data/chapters/Manga pro.json"
        result = manga_pro(url, json_file)
    elif "teamxnovel" in url:
        json_file = "data/chapters/Team-X.json"
        result = teamx(url, json_file)
    elif "lekmanga" in url:
        json_file = "data/chapters/mangalek.json"
        result = mangalek(url, json_file)
    elif "3asq" in url:
        json_file = "data/chapters/3asq.json"
        result = _3asq(url, json_file)
    else:
        result = {"error": "المصدر غير متوفر"}
        
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        image_urls, title, next_chapter_link, prev_chapter_link = result
        
    return image_urls, title, next_chapter_link, prev_chapter_link
