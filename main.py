from app import app
from app import db
import view
from posts.blueprint import posts

app.register_blueprint(posts, url_prefix='/')

if __name__ == '__main__':
    app.run()