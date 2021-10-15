"""Post admin classes"""

# Django
from django.contrib import admin

# Models 
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post in site admin. With this
    class help a modify the ui in site admin"""

    list_display = ('profile_id', 'title', 'photo', )