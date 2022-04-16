import ast
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

with open('data/mnre.txt', 'r') as f:
    datas = f.read().split('\n')
datas = [ast.literal_eval(i) for i in datas]

@app.get("/info/{id}")
async def read_item(request: Request, id: str):
    return datas[int(id)]

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    photo_images = open('images/'+id, "rb")
    return StreamingResponse(photo_images, media_type="image/jpg")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "total": len(datas)})

