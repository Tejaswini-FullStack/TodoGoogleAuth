from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("", views.todo_home, name="todo-home"),
    path("update/<int:id>/", views.update_task, name="update-task"),
    path("delete/<int:id>/", views.delete_task, name="delete-task"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("logout-page/", views.logout_page, name="logout-page"),

]
