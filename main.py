from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles # 정적파일 
from fastapi.templating import Jinja2Templates  # 템플릿화

from pydantic import BaseModel  # 모델링
from typing import Optional # 옵션
from starlette.responses import JSONResponse

from urllib import parse    # 데이터 url 인코딩

import auth # 인증 모듈 호출

class Item(BaseModel):
    user_id : str = None
    user_pwd : str = None



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name = "static")
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def page(request : Request):
    return templates.TemplateResponse("index.html", {"request":request})    # 기본화면

@app.get("/login/", response_class=HTMLResponse)
async def login(request : Request):
    id = ""
    pwd = ""
    return templates.TemplateResponse("login.html", {"request":request, "id":id, "pwd":pwd})    # 로그인화면

@app.post("/login/", response_class=HTMLResponse)
async def login_auth(request : Request, id : str = Form(...), pwd : str = Form(...)):
    info = {"id" : id, "pwd" : pwd}
    result = auth.user_login_compare(info["id"], info["pwd"])
    if result == "0" or result == "2":
        return "Bad"
        # return RedirectResponse("/login/")
    else :
        return "Good"
        # return RedirectResponse("/")
    # parse.urlencode(info) # 인코딩하여 값 전송
    # templates.TemplateResponse("index.html", {"request":request, "id" : id})

"""
@app.get("/post", response_class=HTMLResponse)
async def post_test(request:Request):
    id = ""
    pwd = ""
    return templates.TemplateResponse("post.html", {"request":request, "id":id, "pwd":pwd})

@app.post("/post")
async def post_test(request:Request, id: str = Form(...), pwd:str = Form(...)):
    return id + pwd
"""