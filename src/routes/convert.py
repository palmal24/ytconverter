from fastapi import APIRouter
from converter.youtube import YoutubeAudioConverter, YoutubeVideoConverter
from fastapi.responses import HTMLResponse, FileResponse

__all__ = ["converter_router"]


_YOUTUBE_PREFIX = "https://www.youtube.com/watch?v="

converter_router = APIRouter()


@converter_router.get("/convert-youtube-video/{id}")
def converter(id: str):    
    link = _YOUTUBE_PREFIX + id
    if len(id) != 11:
        return link
    
    yt = YoutubeAudioConverter(link)
    res = yt.convert()
    return res

@converter_router.get("/", response_class=HTMLResponse)
def get_homepage():
    return FileResponse('static/index.html')
