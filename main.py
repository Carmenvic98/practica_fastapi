from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse #devolver valores html 



app = FastAPI()
@app.get("/", tags=['home'])
def read_root():
    return HTMLResponse('<h1> Hello World </h1>')