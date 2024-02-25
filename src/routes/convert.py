from fastapi import APIRouter, Request
from converter import YoutubeAudioConverter, YoutubeVideoConverter
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

__all__ = ["converter_router",]


_YOUTUBE_PREFIX = "https://www.youtube.com/watch?v="

converter_router = APIRouter()


@converter_router.get("/convert-youtube-audio/{id}")
def converter_audio(id: str):    
    link = _YOUTUBE_PREFIX + id
    if len(id) != 11:
        return link + " :: enter valid youtube id"

    yt = YoutubeAudioConverter(link)
    res = yt.convert()
    return res

@converter_router.get("/convert-youtube-video/{id}")
def converter_video(id: str):    
    link = _YOUTUBE_PREFIX + id
    if len(id) != 11:
        return link + " :: enter valid youtube id"

    yt = YoutubeVideoConverter(link, 22)
    res = yt.convert()
    return res

@converter_router.get("/")#, response_class=HTMLResponse)
def get_homepage():#request: Request, id: str):
    return {"msg": "OK"}
    #return Jinja2Templates.get_template()#FileResponse('static/index.html')
