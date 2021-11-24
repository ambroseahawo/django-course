from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Your title"
    }))  # default required = True
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Your description",
        "class": "new-class name",
        "id": "input-id",
        "rows": 20,
        "cols":
        120
    }))
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")

        if "XTER" in title:
            return title
        else:
            raise forms.ValidationError("Your title should contain the chosen word")
        


class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={
                    "placeholder": "Your title"
    })) # default required = True
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
                    "placeholder": "Your description",
                    "class": "new-class name",
                    "id": "input-id",
                    "rows": 20,
                    "cols":
                    120
    }))
    price       = forms.DecimalField(initial=199.99)