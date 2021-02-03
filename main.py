from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from urllib import parse

import auth

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name = "static")
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def page(request : Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.get("/login/", response_class=HTMLResponse)
async def login(request : Request):
    return templates.TemplateResponse("login.html", {"request":request})

@app.get("/login/auth", response_class=HTMLResponse)
async def login_auth(request : Request, id : str, pwd : str):
    info = {"id" : id, "pwd" : pwd}
    result = auth.compare(info["id"], info["pwd"])
    return result
    # parse.urlencode(info) # 인코딩하여 값 전송
    # templates.TemplateResponse("index.html", {"request":request, "id" : id})