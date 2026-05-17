from fastapi import Depends, FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, HttpUrl



class URLRequest(BaseModel):
    url : HttpUrl

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get('/')
def get_home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="home.html",
    context={"request": request}
)


@app.post('/startprocess')
def start_test(url: str = Form(...)):
    original_url = url 
    print(original_url, flush=True)
    return {"Message": "Process has been started"}  