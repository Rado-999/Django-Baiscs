from django.urls import path

from DemoProject1.demoapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form_view, name='forms'),
    # path('create/',views.created_view, name='created_view'),
    # path('error/',views.error_view, name='error_view')
]