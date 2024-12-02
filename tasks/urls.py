from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailAPIView, TaskCompleteAPIView

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', TaskCompleteAPIView.as_view(), name='task-complete'),
]
