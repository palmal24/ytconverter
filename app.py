from flask import Flask
from core.converter import YoutubeAudioConverter

_YOUTUBE_PREFIX = "https://www.youtube.com/watch?v="

app = Flask(__name__)


@app.route("/convert-mp3/<id>")
def converter(id):
    link = _YOUTUBE_PREFIX + id
    if len(id) != 11:
        return link
    
    yt = YoutubeAudioConverter(link)
    res = yt.convert()
    return res
    
    
@app.route("/")
def home():
    return "<h1>Test Home</h1>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)
