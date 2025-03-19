from fastapi import FastAPI
from api.routes.todo import todo_router
# Импорт роутера todo_router из модуля todo.py в папке api/routes.
# Благодаря наличию __init__.py в папках, Python распознаёт их как модули.

app = FastAPI()
app.include_router(todo_router)
# include_router() — это метод FastAPI, который позволяет подключить роутер к основному приложению.
# В данном добавление всех маршрутов из todo_router в приложение.


@app.get("/")
def index():
    return {"status": "todo api is running"}
