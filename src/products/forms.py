from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(
                    attrs = {
                        'placeholder':'Your title here'
                    }
                )
            )
    # email = forms.EmailField()
    description = forms.CharField(required=False, 
                    widget=forms.Textarea(
                        attrs={
                            'rows':20,
                            'cols':100,
                            'class':'new class '
                        }
                    )
                )
    price       = forms.DecimalField(initial=100)
    class Meta:
        
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    # def clean_title(self,*args,**kwargs):
    #     title = self.cleaned_data.get('title')
    #     if 'cfe' not in title:
    #         raise forms.ValidationError('This is invalid')
    #     return title
    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            raise forms.ValidationError('email is invalid')
        return email

class RawProductForm(forms.Form):
    title       = forms.CharField(
                        widget=forms.TextInput(
                            attrs=
                            {
                                'placeholder':'Your Title here'
                        }
                    )
                )
    description = forms.CharField(required=False, 
                        widget=forms.Textarea(
                            attrs={
                                'rows':20,
                                'cols':100,
                                'class':'new class '
                            }
                        )
                    )
    price       = forms.DecimalField(initial=100)
