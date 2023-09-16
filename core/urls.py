from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI

from app.api.v1.views import router as api_tasks

api = NinjaAPI(
    title='API',
    version='1.0',
    description='API de Testes'
)

api.add_router('/tasks/', api_tasks)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', api.urls)
]
