from django.urls import path

from DjangoTemplates.TemplateAdvanced import views

urlpatterns = [
    path('', views.home_page_view, name='index'),
    path('user/', views.user_page_view, name= 'user_page_view')
]