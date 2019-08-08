from flask import Flask, abort, send_file
from download import YoutubeDownloader, Options
import os

app = Flask(__name__)

@app.route("/<videoId>")
def download(videoId):
    try:
        filename = YoutubeDownloader.download(videoId, Options.AUDIO)
        if not filename: raise
        return send_file(os.path.join(".", filename))
    except YoutubeDownloader.VideoNotFoundException:
        abort(404)
    except Exception:
        abort(500)

@app.route("/health")
def healthCheck():
    return "I'm OK!"
