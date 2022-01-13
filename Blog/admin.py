from django.contrib import admin

from Blog.models import Post,Celebrity,CelebrityAdmin, Reporter

# Register your models here.

admin.site.register(Post)
admin.site.register(Reporter)
admin.site.register(Celebrity, CelebrityAdmin)