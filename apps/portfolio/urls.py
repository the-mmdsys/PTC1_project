from django.urls import path
from .views import CategoryListView, ProjectListView, ProjectDetailView

app_name = 'portfolio'

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
]