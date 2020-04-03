from django.shortcuts import render
from django.views.generic.list import ListView
from myapp.models import Notice, Profile, Course
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    return render(request, "home.html")



class  NoticeListView(ListView):
    model = Notice

@method_decorator(login_required, name="dispatch")   
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["branch", "sem", "marks_10", "marks_12", "marks_aggr", "rn", "pn", "myimg"]


class  CourseListView(ListView):
    model = Course