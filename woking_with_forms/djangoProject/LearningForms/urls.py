from django.urls import path

from djangoProject.LearningForms import views

urlpatterns = [
    path('', views.index, name='index'),
    path('created', views.index, name='create_view'),
    path('model', views.modelindex, name='create_model'),
    path('update/<int:pk>/', views.update_student, name='update_student')
]