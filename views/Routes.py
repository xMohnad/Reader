from flask import request, Blueprint, render_template, url_for, redirect, flash
from src.check.check import checkselection

routes = Blueprint('main', __name__)

def process_url(url):
    result = checkselection(url)
    if isinstance(result, dict) and 'error' in result:
        error_message = result['error']
        flash(error_message, 'danger')
        return redirect(url_for('main.index'))
    image_urls, title, next_chapter_link, prev_chapter_link = result
    return render_template('index.html', image_urls=image_urls, next_chapter_link=next_chapter_link, prev_chapter_link=prev_chapter_link, title=title)

@routes.route('/')
def index():
    url = request.args.get('url', '')
    if url:
        return process_url(url)
    return render_template('index.html')

@routes.route('/next')
def nextchap():
    url = request.args.get('next', '')
    if url:
        return process_url(url)
    return render_template('index.html')

@routes.route('/prev')
def prevchap():
    url = request.args.get('prev', '')
    if url:
        return process_url(url)
    return render_template('index.html')
