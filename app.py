#https://flask.palletsprojects.com/en/2.2.x/quickstart/
#server structures (backend development)
#importing the template of the server
# from flask import Flask, render_template

# app = Flask(__name__, template_folder='templates')  #app is where it hosts #homepage and then :5000 port (http://127.0.0.1:5000 - local host)

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/hello') #mapping of that URL and ignoring the domain to that method (def hello_world) #route of my pages
def hello_world(): #app route - /hello/hello/hello/hello for example [it is just a string matching]
    return 'Hello World!'

@app.get('/') #url and port
def default():
    return 'default!'

# @app.get('/todo', response_class=HTMLResponse)
# def todo():
#     return render_template('todo.html', args=args)

@app.get("/todo", response_class=HTMLResponse)
async def read_item(request: Request):
    args = {'first_name': 'Min','last_name': 'Lee'} #{} meaning - this object is going to be a dictionary
    return templates.TemplateResponse("todo.html", {"request": request, "args":args})


#what is returned by this then? the only you can be returned is a STRING
# if __name__ == '__main__':
#     import sys
#     print(sys.path)
#     print("hello world") #redefining the start of the program
#     app.run(port='5000')

#Flask - consider webpages as templates, when looking for files it looks at the folder structure
#jinja2 - built into Flask it is a syntax that allows - templatize our HTML (jinja structure)


