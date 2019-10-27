from flask import Flask, abort, send_file, request
from download import YoutubeDownloader, Options
from clean import Clean
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/<videoId>")
def download(videoId):
    try:
        option = Options.AUDIO if request.args.get("option", "") == "audio" else Options.BOTH
        filename = YoutubeDownloader.download(videoId, option)
        if not filename: raise
        Clean.scheduleRemove(filename)
        return send_file(os.path.join(".", filename))
    except YoutubeDownloader.VideoNotFoundException:
        abort(404)
    except Exception as e:
        app.logger.error(e)
        abort(500)

@app.route("/health")
def healthCheck():
    return "I'm OK!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
