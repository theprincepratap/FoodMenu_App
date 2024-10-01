from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        models = Item
        fields = ['item_name', 'item_description', 'item_price', 'item_image']