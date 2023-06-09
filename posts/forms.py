from django import forms
from .models import PostTag


class PostTagForm(forms.ModelForm):
    class Meta:
        model = PostTag
        fields = ["title"]
