from django.urls import path

from . import views

app_name='projects'

urlpatterns = [
	path('create/', views.create_project, name='create'),
	path('<pk>/', views.project_detail, name='project'),
	path('edit/<pk>/', views.edit_project, name='edit')
]