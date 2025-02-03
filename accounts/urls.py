
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registration,name='registration'),
    path('login/',views.login_page,name='login'),
    path('',views.home,name='home'),
    path('student_profile/<str:pk>/',views.student_profile,name='student_profile'),
    path('logout',views.logout_user,name='logout')
]