from pydantic import BaseModel, Field
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from api.models.todo import Todo
# BaseModel	Родительский класс для создания Pydantic-моделей
# Field	Позволяет задавать валидацию и метаданные для полей модели
# Optional	Указывает, что значение поля может быть None
# pydantic_model_creator	Автоматически создаёт Pydantic-модель на основе модели Tortoise ORM


GetTodo = pydantic_model_creator(Todo, name='Todo')
# pydantic_model_creator — это функция из Tortoise ORM, которая создаёт Pydantic-схему автоматически на основе ORM-модели.
# Сейчас ты передаёшь None вместо модели, потому что модель в ORM пока не создана.
# Когда ты создашь модель в Tortoise ORM, сюда нужно будет передать ссылку на неё:


class PostTodo(BaseModel):
    # ... — обязательное поле (если не указано, FastAPI вернёт ошибку).
    task: str = Field(..., max_length=100)
    done: bool


class PutTodo(BaseModel):
    task: Optional[str] = Field(None, max_length=100)
    done: Optional[bool]
