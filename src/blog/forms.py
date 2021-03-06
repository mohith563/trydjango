from django import forms

from .models import Article

class ArticleModelForm(forms.ModelForm):
    # title = forms.CharField(widget = forms.TextInput(
    #     attrs = {
    #         'placeholder':'Your Title here'
    #     }
    # ))
    # article = forms.CharField(required=False, 
    #                 widget=forms.Textarea(
    #                     attrs={
    #                         'rows':20,
    #                         'cols':100,
    #                         'class':'new class '
    #                     }
    #                 )
    #             )
    # author = forms.CharField(required = True,
    #                             max_length=30)
    class Meta:
        model = Article
        fields = [
            'title',
            'article',
            'author'
        ]                                

