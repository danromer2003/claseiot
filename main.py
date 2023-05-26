from fastapi import FastAPI
from pydantic import BaseMode1


app=FastAPI()


@app.get("/")
def index(): 
        return "Hola a todos, quieres saber de spider man nenes"


