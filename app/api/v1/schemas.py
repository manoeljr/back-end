from ninja import ModelSchema

from app.models import Task


class TaskSchemaIn(ModelSchema):
    title: str
    description: str
    completed: bool

    class Config:
        model = Task
        model_fields = ['title', 'description', 'completed']


class TaskSchemaOut(ModelSchema):
    id: int
    title: str
    description: str

    class Config:
        model = Task
        model_fields = ['id', 'title', 'description']
