from django.urls import path
from . import views

app_name ='posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('<slug:slug>', views.post_page, name="page"),  # the path converters on the left 右邊是接收的參數名slug
]