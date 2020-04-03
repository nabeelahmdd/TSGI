from django.shortcuts import render
from django.views.generic.list import ListView
from myapp.models import Notice

# Create your views here.
def home(request):
    return render(request, "home.html")

class  NoticeListView(ListView):
    model = Notice