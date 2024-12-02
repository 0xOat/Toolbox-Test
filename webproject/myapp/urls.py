from django.urls import path
from .views import *
urlpatterns = [
    path("del/<int:pk>/", DelData.as_view()),
    path("done/", done, name="done"),
]
