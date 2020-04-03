from django.urls import path
from myapp import views

urlpatterns = [

    path('home/', views.home),
    path('notice/', views.NoticeListView.as_view()),
    path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url="/myapp/notice")),
]