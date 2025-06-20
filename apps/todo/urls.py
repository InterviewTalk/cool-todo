
from django.urls import path, include


from rest_framework import routers
from apps.todo.views import TodoViewSet

todo_router = routers.DefaultRouter()
todo_router.register(r'todo', TodoViewSet)

urlpatterns = [
    # add the DRF endpoints
    path('api/', include(todo_router.urls)),
]