from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'date', 'is_published', 'category', 'comments', 'likes')
    list_display_links = ('id', 'task')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Likes)
admin.site.register(Comments)

# admin.site.register()
# admin.site.register()
