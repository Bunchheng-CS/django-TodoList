from django.urls import path
from . import views

app_name = 'base'
urlpatterns =[
    path('login/',views.login_page,name='login_page'),
    path('register/',views.register_page,name='register_page'),
    path('logout/',views.logout_page,name='logout_page'),


    path('',views.home_page,name='home_page'),
    path('create_task/',views.create_task,name='create_task'),
    path('update_task/<int:pk>/',views.update_task,name='update_task'),
    path('detele_task/<int:pk>/',views.delete_task,name='delete_task'),

]