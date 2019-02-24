from django.urls import path

from . import views

app_name='projects'

urlpatterns = [
	path('create/', views.create_project, name='create'),
	path('notification/', views.notification, name='notification'),
	path('application/', views.application_list, name='application'),
    path('application/<pk>/accept/', views.accept_application, name="accept"),
    path('application/<pk>/reject/', views.reject_application, name="reject"),
    path('application/accept/', views.accept_application_list, name="accept_application"),
    path('application/reject/', views.reject_application_list, name="reject_application"),
    path('application/new/', views.new_application_list, name="new_application"),
	path('<pk>/', views.project_detail, name='project'),
	path('edit/<pk>/', views.edit_project, name='edit'),
	path('<pk>/delete/', views.delete_project, name='delete'),
	path('<pk>/apply/<position_pk>', views.apply, name='apply'),
]