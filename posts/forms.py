"""Post Forms."""

# Django
from django import forms

# Models
from posts.models import Post

class PostForm(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Fomr settings."""

        model = Post
        fields = ['profile_id','title','photo']