from django import forms
from .models import Comment


class CommentBox(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
