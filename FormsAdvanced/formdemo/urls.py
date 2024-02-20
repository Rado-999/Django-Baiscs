from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from FormsAdvanced.formdemo import views

urlpatterns = [
    path('', views.index, name='home'),
    path('created/', views.index, name='created'),
    path('fewforms/' , views.manage_people, name='manage_people')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
