from app import app
from flask import render_template


@app.route('/page')
def index():
    return render_template('index.html')