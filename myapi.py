# import FastAPI class from fastapi
from fastapi import FastAPI

# create object of FastAPI
app =  FastAPI()

# create route and define function
@app.get('/')
def index():
    return {'name':'FastAPI'}
