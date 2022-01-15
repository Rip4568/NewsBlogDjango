from django.urls import path,include,re_path
from .views import home,post
urlpatterns = [
    path('',home),
    path('<int:my_id>',post),
    #re_path(r'^static/<int:my_id$',post)
]