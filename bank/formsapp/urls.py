from . import views
from django.urls import path

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('details',views.details,name='details'),
    path('add',views.add,name='add'),
    path('logout',views.logout,name='logout'),
    path('accepted',views.accepted,name='accepted'),
    path('user_form',views.user_form,name='user_form'),
    path('ajax/load-branches', views.load_branches, name='load_branches'),

]