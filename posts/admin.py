from django.contrib import admin
from .models import Post, PostTag, PostCategory


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "category", "get_tags", "date_create", "image")

    def get_tags(self, obj):
        tags = obj.tags.all()
        return "\n".join([str(t) for t in tags])


admin.site.register(Post, PostAdmin)
admin.site.register(PostTag)
admin.site.register(PostCategory)
