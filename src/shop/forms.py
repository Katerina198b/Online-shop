# -*- coding: utf-8 -*-v

from django import forms

class ShopListForm(forms.Form):

    search = forms.CharField(required=False, label='Поиск по имени магазина')

class ShopForm(forms.Form):

    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
#не использую
class PublishForm(forms.Form):

    pub = forms.BooleanField(label="Опубликовать")
