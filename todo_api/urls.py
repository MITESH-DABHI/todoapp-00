from django.urls import path
from .views import Home,TodoListApiView,TodoDetailApiView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/',Home.as_view()),
    path('api/',TodoListApiView.as_view()),
    path('api/<int:todo_id>/',TodoDetailApiView.as_view()),
]
