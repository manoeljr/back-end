from ninja import Router
from .schemas import TaskSchemaIn, TaskSchemaOut
from app.models import Task


router = Router()


@router.get("", response=list[TaskSchemaOut])
def list_tasks(request):
    tasks = Task.objects.all()
    return tasks


@router.post("", response=TaskSchemaOut)
def create_task(request, task: TaskSchemaIn):
    new_task = Task(**task.dict())
    new_task.save()
    return new_task
