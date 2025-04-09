from django.urls import path
from . import views
from .views import TaskList,TaskDetail,CreateTask,UpdateTask,DeleteTask,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/',CustomLoginView.as_view(),name="login"),
    path('register/',RegisterPage.as_view(),name="register"),
    path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
    path('',TaskList.as_view(),name="tasks"),
    path('task/<int:pk>/',TaskDetail.as_view(),name="task"),
    path('create-task/',CreateTask.as_view(),name="task-create"),
    path('update-task/<int:pk>/',UpdateTask.as_view(),name="task-update"),
    path('delete-task/<int:pk>/',DeleteTask.as_view(),name="task-delete"),
    
    # path('logout/',CustomLogoutView.as_view(),name="logout"),
]
