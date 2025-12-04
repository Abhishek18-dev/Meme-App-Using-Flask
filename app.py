from flask import Flask, render_template
import json
import requests
import os

app = Flask(__name__)


def meme_get():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@app.route('/', methods=["GET", "POST"])
def index():
    meme_pic, subreddit = meme_get()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)


if __name__ == "__main__":
    # Debug mode should only be enabled for local development
    # In production, use a proper WSGI server like Gunicorn instead
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)
