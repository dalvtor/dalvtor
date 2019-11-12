from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('<int:year>/<int:month>/', views.PostArchiveView.as_view(month_format='%m'), name="post-archive"),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
]
