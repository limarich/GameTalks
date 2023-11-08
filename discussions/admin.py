from django.contrib import admin

from .models import Comment,Tag,Post,Thread

admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
