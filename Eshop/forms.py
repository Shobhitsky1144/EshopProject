from django import forms
from Eshop.models import add_product

class add_product_form(forms.ModelForm):
    class Meta:
        model=add_product
        fields=["product_name","product_category","product_price","sale_price","product_images","details"]
