from django.urls import path
from django.views.generic.base import RedirectView
from myapp import views

urlpatterns = [

    path('home/', views.home),
    path('notice/', views.NoticeListView.as_view()),
    path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url="/myapp/notice")),
    path('course/', views.CourseListView.as_view()),
    path('contact/', views.contact),
    path('about/', views.about),
    path('', RedirectView.as_view(url="notice/")),
]