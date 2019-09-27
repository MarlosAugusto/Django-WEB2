from django import forms
from .models import Comment

class NewForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = {'Comentario'}