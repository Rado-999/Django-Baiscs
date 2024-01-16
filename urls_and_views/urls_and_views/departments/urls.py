from django.urls import path, include

from urls_and_views.departments.views import index1, welcome_page, index2, index3, index4, show_department_by_id, \
    show_deparment_by_str, show_deparment_by_slug

urlpatterns = (
    path('<int:department_id>',show_department_by_id),
    path('<str:department_name>', show_deparment_by_str),
    path('<slug:slug>', show_deparment_by_slug),
    path('',welcome_page),
)