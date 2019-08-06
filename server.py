from flask import Flask, abort
from download import YoutubeDownloader
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def download():
    try:
        YoutubeDownloader.download("")
        return
    except YoutubeDownloader.VideoNotFoundException:
        abort(404)
    except Exception:
        abort(500)
