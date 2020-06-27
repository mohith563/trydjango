from django.urls import path

from .views import (my_fbv, 
                    CourseView, 
                    CourseListView, 
                    MyListView,
                    CourseCreateView,
                    CourseUpdateView,
                    CourseDeleteView)

app_name='courses'
urlpatterns=[
    path('<int:id>/delete/',CourseDeleteView.as_view(),name='course-delete'),
    path('<int:id>/update/',CourseUpdateView.as_view(),name='course-update'),
    path('create/',CourseCreateView.as_view(),name='course-create'),
    # path('',MyListView.as_view(template_name='contact.html'),name='course-list'),
    # path('',my_fbv,name='course-list'),
    path('<int:id>/',CourseView.as_view(),name='course-detail'),
    path('',CourseListView.as_view(),name='course-list'),
]