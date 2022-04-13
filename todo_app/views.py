from django.shortcuts import render
from django.views import View
# from todo_api.models import Todo

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request,"base.html")   