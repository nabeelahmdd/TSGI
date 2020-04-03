
from django.urls import path

from myapp import views









urlpatterns = [

    path('home/', views.home),

    path('notice/', views.NoticeListView.as_view()),



]