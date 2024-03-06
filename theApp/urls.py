from django.urls import path
from . import views
app_name="theApp"
urlpatterns=[
    path("add", view.add, name="add")
]