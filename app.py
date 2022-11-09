from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/') #url and port
def default():
    return 'default!'

@app.get("/todo", response_class=HTMLResponse)
async def read_item(request: Request):
    args = {'first_name': 'Rachel','last_name': 'Lee'}
    return templates.TemplateResponse("todo.html", {"request": request, "args":args})