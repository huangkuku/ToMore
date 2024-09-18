from django import forms 
from . import models 

class CreatePost(forms.ModelForm):
    class Meta:  # nest class Model
        model = models.Post
        fields = ['title', 'body', 'slug', 'banner']