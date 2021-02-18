from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        models = models.Article
        fields = ['title','body','slug','thumb']
