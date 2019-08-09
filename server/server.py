from flask import Flask, abort, send_file, request
from download import YoutubeDownloader, Options
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route("/<videoId>")
def download(videoId):
    try:
        option = Options.AUDIO if request.args.get("option", "") == "audio" else Options.BOTH
        filename = YoutubeDownloader.download(videoId, option)
        if not filename: raise
        return send_file(os.path.join(".", filename))
    except YoutubeDownloader.VideoNotFoundException:
        abort(404)
    except Exception as e:
        app.logger.error(e)
        abort(500)

@app.route("/health")
def healthCheck():
    return "I'm OK!"
