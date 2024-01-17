from django.urls import path, include

from urls_and_views.departments.views import welcome_page, show_department_by_id, show_deparment_by_str, \
    show_deparment_by_slug, create_department, edit_department, delete_department

urlpatterns = (
    path('<int:department_id>',show_department_by_id),
)