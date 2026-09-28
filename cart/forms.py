from django import forms

class CartAddProductForm(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]
    
    quantity = forms.TypedChoiceField(
        choices=QUANTITY_CHOICES,
        coerce=int,              
        initial=1,                
        label='Количество',       
        widget=forms.Select(attrs={'class': 'form-select', 'style': 'width: 100px;'})  
    )
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)