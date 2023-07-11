from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from posts.views import posts, get_post, get_tag_post, add_post_tag, \
    create_post_tag, search_post, add_post, delete_post, update_post, likes

urlpatterns = [path('get_posts/', posts, name="posts"),
               path('get_posts/<int:id>/', get_post, name="get_post"),
               path('get_posts/<str:title>/', get_tag_post, name="get_tag"),
               path('add_PostTag/', add_post_tag, name="add_post_tag"),
               path('create_PostTag/', create_post_tag, name="create_post_tag"),

               path('add_post/', add_post, name="add_post"),
               path('search_post/', search_post, name="search_post"),
               path('delete_post/<int:id>/', delete_post, name="delete_post"),

               path('update_post/<int:id>', update_post, name="update_post_by_id"),
               path('likes/<int:id>', likes, name="likes")
               ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
