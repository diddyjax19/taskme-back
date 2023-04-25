from rest_framework.routers import DefaultRouter
from .views import TaskCreationUpdationView,ProjectTaskListView,CreateSubTaskView
from django.urls import path,include

router = DefaultRouter()
router.register("",TaskCreationUpdationView,basename="task")

urlpatterns = [
    path("",include(router.urls)),
    path("all/<int:project_id>/<str:me>/",ProjectTaskListView.as_view()),
    path("all/<int:project_id>/",ProjectTaskListView.as_view()),
    path("sub-task/<int:task_id>/",CreateSubTaskView.as_view()),
]
