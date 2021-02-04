from fastapi import FastAPI, Request, Form, Header
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.responses import JSONResponse
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles # 정적파일 
from fastapi.templating import Jinja2Templates  # 템플릿화

from pydantic import BaseModel  # 모델링
from typing import Optional # 데이터 옵션
from urllib import parse    # 데이터 url 인코딩

import auth # 인증 모듈 호출

class Item(BaseModel):
    user_id : str = None
    user_pwd : str = None

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name = "static")
templates = Jinja2Templates(directory="templates")

@app.get('/')
async def page(request : Request):
    return templates.TemplateResponse("/index.html", {"request":request})    # 기본화면

@app.post('/')
async def page(request : Request):
    return templates.TemplateResponse("/index.html", {"request":request})    # 기본화면

@app.get('/login')
async def login(request : Request):
    id = ""
    pwd = ""
    return templates.TemplateResponse("/login.html", {"request":request, "id":id, "pwd":pwd, "token": "0"})    # 로그인화면

@app.post('/login', response_class=HTMLResponse)
async def login_auth(request : Request, response : Response, id : str = Form(...), pwd : str = Form(...), x_token : Optional[str] = Header(None)):
    info = {"id" : id, "pwd" : pwd}
    result = auth.user_login_compare(info["id"], info["pwd"])
    if result == "0" or result == "2":
        return templates.TemplateResponse("/login.html", {"request":request, "id":id, "pwd":pwd, "error":"로그인 실패"})
    else :
        content = {"msg":"msg"}
        headers = {"Token":result}
        # response.headers["X-Token"] = result
        return templates.TemplateResponse("/index.html", {"request":request}, headers=headers)
        # return RedirectResponse("/")
    # parse.urlencode(info) # 인코딩하여 값 전송
    # templates.TemplateResponse("index.html", {"request":request, "id" : id})

@app.get('/auth')
async def auth_check(request : Request, x_token : str):
    return x_token
