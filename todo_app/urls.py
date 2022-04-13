from django.urls import path
from .views import Home

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',Home.as_view()),
    
]
