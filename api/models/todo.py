from tortoise.models import Model
# Model — это базовый класс в Tortoise ORM.
# Когда ты наследуешь от Model, Tortoise автоматически создаёт таблицу в базе данных на основе структуры этого класса.
# Этот класс управляет операциями CRUD (Create, Read, Update, Delete).
from tortoise.fields import IntField, BooleanField, CharField
# IntField	Целочисленное поле (INTEGER)
# BooleanField	Логическое поле (BOOLEAN)
# CharField	Текстовое поле (VARCHAR)


class Todo(Model):
    id = IntField(pk=True)
    task = CharField(max_length=100, null=False)
    done = BooleanField(default=False, null=False)


# IntField → Создаёт целочисленный столбец в таблице.
# pk=True → Указывает, что это первичный ключ (PRIMARY KEY) для таблицы.
# Это значит, что каждое значение id будет уникальным и автоматически индексироваться.
# Tortoise сам создаст автоинкрементирующееся поле (AUTO_INCREMENT в PostgreSQL и MySQL).
