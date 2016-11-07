# -*- coding: utf-8 -*-v
from django import forms

class CommentForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    author = forms.CharField()
