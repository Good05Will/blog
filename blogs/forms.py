from django import forms
from .models import Topic, Note

class PostForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']
        labels = {'title':''}


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}