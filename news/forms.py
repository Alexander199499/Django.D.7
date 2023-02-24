from django import forms
from django.core.exceptions import ValidationError
from .models import *


class ProductForm(forms.ModelForm):
    article = 'AR'
    news = 'NE'

    POST_TYPES = [
        (article, 'Статья'),
        (news, 'Новость')
    ]


    text = forms.Textarea()
    author = forms.ModelChoiceField(label='Имя автора', queryset = Author.objects.all())
    title = forms.CharField(label='Заголовок')
    post_type = forms.ChoiceField(label='Тип поста', choices=POST_TYPES)

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'post_type'
        ]
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")
        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )
        return cleaned_data