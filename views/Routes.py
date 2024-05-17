from flask import request, Blueprint, render_template, url_for
from src.check import checkselection

routes = Blueprint('main', __name__)

@routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        chapter_link = request.form['chapter_link']
        image_urls, title, next_chapter_link, prev_chapter_link = checkselection(chapter_link)
        if title is None:
            title = "المصدر غير متوفر"
            return render_template('index.html', title=title)
        
        return render_template('index.html', image_urls=image_urls, next_chapter_link=next_chapter_link, prev_chapter_link=prev_chapter_link, title=title)
    return render_template('index.html')

@routes.route('/next', methods=['POST'])
def nextchap():
    if request.method == 'POST':
        next_chapter = request.form.get('next_chapter')
        image_urls, title, next_chapter_link, prev_chapter_link = checkselection(next_chapter)
        
        return render_template('index.html', image_urls=image_urls, next_chapter_link=next_chapter_link, prev_chapter_link=prev_chapter_link, title=title)
    return render_template('index.html')
    
@routes.route('/prev', methods=['POST'])
def prevchap():
    if request.method == 'POST':
        prev_chapter = request.form.get('prev_chapter')
        image_urls, title, next_chapter_link, prev_chapter_link = checkselection(prev_chapter)
        
        return render_template('index.html', image_urls=image_urls, next_chapter_link=next_chapter_link, prev_chapter_link=prev_chapter_link, title=title)
    return render_template('index.html')
    
