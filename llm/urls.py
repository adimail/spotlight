from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('write/', views.write_view, name='write'),
    path('ask/', views.ask_view, name='ask'),
    path('docs/', views.docs_view, name='docs'),
]