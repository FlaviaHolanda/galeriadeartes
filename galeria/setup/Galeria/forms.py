from django import forms
from .models import Image, Comment


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("title", "image")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('image', 'name' ,'comment')