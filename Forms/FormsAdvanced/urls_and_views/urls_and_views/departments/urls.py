from django.urls import path, include

import urls_and_views.departments.views as views

urlpatterns = (
    path('department/<int:department_id>',views.show_department_by_id),
    path('department/CRUD',views.crud_page),
    path('department/CRUD/', include([
        path('create', views.create_department),
        path('edit', views.edit_department),
        path('delete', views.delete_department)
    ])),
)


