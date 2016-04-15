# -*- coding: utf-8 -*-v
from django import forms
'''
принимает данные из запроса, валидирует их относительно внутренних полей,
которые мы создали. ПРиводит нас к нужному представлению на языке питон

формочки джанго умеют сами себя печатать
'''
class ProductListForm(forms.Form):

    #quantity = forms.ChoiceField(choices=)
    search = forms.CharField(required=False, label="Поиск по имени товара")
    sort_field = forms.ChoiceField(choices=(('changed_at', 'Дата изменения'),
            ('created_at', 'Дата создания')),required=False, label='Сортировка ')

    # возвращает словарик cleaning_data
    # либо выбрасывает exception
    #def clean(self):

        #raise forms.ValidationError('я не хочу искать и сортировать')

    #def clean_search(self):
    #    search = self.cleaned_data('search')
    #   raise forms.ValidationError('я не хочу искать')
    #    return search

    class Meta:
        verbose_name = "lollolo"

class ProductForm(forms.Form):

    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    #widget - класс отвечающий за показ элементов ввода
    #class Meta:

class CommentForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    author = forms.CharField()
