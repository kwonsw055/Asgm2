from django.urls import path
#from .views import IndexView, DetailView, WriteView, EditView, DeleteView
from . import views
urlpatterns = [
	#path('',IndexView.as_view()),
	#path('detail/<int:id>/', DetailView.as_view()),
	#path('write/', WriteView.as_view()),
	#path('edit/<int:id>/', EditView.as_view()),
	#path('delete/<int:id>/', DeleteView.as_view()),
	path('', views.PostListView.as_view(), name='post_list'),
	path('<int:pk>/', views.DetailView.as_view(), name='post_detail'),
	path('write/', views.WriteView.as_view(), name='post_create'),
	path('<int:pk>/edit', views.PostUpdateView.as_view(), name='post_update'),
	path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
]
