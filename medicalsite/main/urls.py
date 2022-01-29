from django.urls import path
from . import views
from main import views as myapp_views

urlpatterns = [
    path('register/', myapp_views.register,name='register'),    
    path('register/save', myapp_views.register_user),   
    path('register/login', myapp_views.login),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('dashboard/logout', views.logout_request,name="logout"),
    path('dashboard/newMed', views.med_create,name="new med"),
    path('dashboard/getMedData/',views.getMedData),
    path('dashboard/addMed', views.add_med,name="addmed"),
    path('dashboard/myMed/',views.my_Med,name="myMed"),
    path('dashboard/myMed/view/',views.view,name="view"),
    path('dashboard/myMed/remove',views.remove,name="remove"),
]