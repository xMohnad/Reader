from flask import Flask
from flask_assets import Bundle, Environment
from views.Routes import routes
import config 

app = Flask(__name__)
app.config.from_object(config)

assets = Environment(app)
css = Bundle('css/bootstrap.min.css', 'css/styles.css', output='gen/packed.css')
js = Bundle('js/script.js', output='gen/packed.js')

assets.register('css_all', css)
assets.register('js_all', js)

app.register_blueprint(routes)

if __name__ == '__main__':
   app.run(debug=app.config["DEBUG"])