from fastapi import APIRouter, HTTPException, status
from api.models.todo import Todo
from api.schemas.todo import GetTodo, PostTodo, PutTodo

todo_router = APIRouter(prefix='/api', tags=['Todo'])

# APIRouter — это специальный объект FastAPI для группировки маршрутов.
# prefix='/api'	Все маршруты будут иметь префикс /api (например, /api/)


@todo_router.get('/')
async def all_todos():
    data = Todo.all()  # возвращает все объекты из таблицы todo.
    # from_queryset() — метод Tortoise ORM для преобразования набора данных в Pydantic-схему.
    return await GetTodo.from_queryset(data)


@todo_router.post('/')
async def post_todo(body: PostTodo):
    # создает новую запись в БД и превращает тело в словарь, исключая значения None.
    row = await Todo.create(**body.dict(exclude_unset=True))
    # возвращает созданную запись в формате Pydantic-схемы.
    return await GetTodo.from_tortoise_orm(row)


@todo_router.put('/{key}')
async def update_todo(key: int, body: PutTodo):
    data = body.dict(exclude_unset=True)
    # проверяет, существует ли задача с таким id.
    exists = await Todo.filter(id=key).exists()
    if not exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Todo not found')
    # обновляет поля задачи в базе данных.
    await Todo.filter(id=key).update(**data)
    # возвращает обновлённый объект.
    return await GetTodo.from_queryset_single(Todo.get(id=key))


@todo_router.delete('/{key}')
async def delete_todo(key: int):
    exists = await Todo.filter(id=key).exists()
    if not exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Todo not found')
    await Todo.filter(id=key).delete()
    return 'Todo deleted successfully'
