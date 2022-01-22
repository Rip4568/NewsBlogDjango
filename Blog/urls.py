from django.urls import path,include,re_path
from .views import home,post
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',home),
    path('<int:my_id>',post),
    #re_path(r'^static/<int:my_id$',post)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)