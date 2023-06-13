from django import forms
from .models import Post, PostTag


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['date_create'] = forms.DateField(
            widget=forms.DateInput(
                format='%d-%m-%Y',
                attrs={'type': 'date'}
            ),
            required=False
        )

    class Meta:
        model = Post
        fields = "__all__"

class PostTagForm(forms.ModelForm):
    class Meta:
        model = PostTag
        fields = ["title"]


