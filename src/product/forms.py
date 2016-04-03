# -*- coding: utf-8 -*-v
from django import forms
'''
принимает данные из запроса, валидирует их относительно внутренних полей,
которые мы создали. ПРиводит нас к нужному представлению на языке питон

формочки джанго умеют сами себя печатать
'''
class ProductListForm(forms.Form):

    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(('id', 'ID'), ('created_at', 'Дата создания')), required=False)

    # возвращает словарик cleaning_data
    # либо выбрасывает exception
    def clean(self):
        raise forms.ValidationError('я не хочу искать и сортировать')

    #def clean_search(self):
    #    search = self.cleaned_data('search')
    #   raise forms.ValidationError('я не хочу искать')
    #    return search

class ProductForm(forms.Form):

    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    #widget - класс отвечающий за показ элементов ввода
    #class Meta:

