from flask import Flask
from flask_assets import Bundle, Environment
from views.Routes import routes
import config 
from dotenv import load_dotenv
import os, random, string

def generate_secret_key(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(random.choices(characters, k=length))
    return key

load_dotenv()
app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', generate_secret_key())
app.config.from_object(config)

assets = Environment(app)
css = Bundle('css/bootstrap.min.css', 'css/styles.css', output='gen/packed.css')
js = Bundle('js/script.js', output='gen/packed.js')

assets.register('css_all', css)
assets.register('js_all', js)

app.register_blueprint(routes)

if __name__ == '__main__':
   app.run(debug=app.config["DEBUG"])