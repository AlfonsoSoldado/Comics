# -*- encoding: utf-8 -*-
from django import forms

class ComicForm(forms.Form):
    comicTitle = forms.CharField(label='Comic')
