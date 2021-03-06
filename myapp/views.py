from django.shortcuts import render
from django.views.generic.list import ListView
from myapp.models import Notice, Profile, Course, Contact
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.views.generic.edit import UpdateView, CreateView
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from datetime import datetime
from django.contrib import messages



# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

class  NoticeListView(ListView):
    model = Notice
    
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
            
        if self.request.user.is_superuser:
            return Notice.objects.filter(Q(subject__icontains =si) | Q(mmsg__icontains =si)).order_by("-id")
        else:
            return Notice.objects.filter(Q(branch=self.request.user.profile.branch)| Q(branch__isnull=True)).filter(Q(subject__icontains =si) | Q(mmsg__icontains =si)).order_by("-id")

@method_decorator(login_required, name="dispatch")   
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["branch", "sem", "marks_10", "marks_12", "marks_aggr", "rn", "pn", "myimg"]


class  CourseListView(ListView):
    model = Course


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contact(name=name, email=email, phone=phone, desc=desc, cr_date=datetime.today())
        
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request, "contact.html")
