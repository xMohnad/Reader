from .mangapro import manga_pro
from .Teamx import teamx
from .Mangalek import mangalek

def checkselection(url):
    if "mangapro" in url and url is not None:
        json_file = "src/seve_data/data/Manga pro.json"
        image_urls, title, next_chapter_link, prev_chapter_link = manga_pro(url, json_file)
    elif "teamxnovel" in url and url is not None:
        json_file = "src/seve_data/data/Team-X.json"
        image_urls, title, next_chapter_link, prev_chapter_link = teamx(url, json_file)
    elif "lekmanga" in url and url is not None:
        json_file = "src/seve_data/data/mangalek.json"
        image_urls, title, next_chapter_link, prev_chapter_link = mangalek(url, json_file)
    else:
        title = None
        return None, title, None, None

    return image_urls, title, next_chapter_link, prev_chapter_link
