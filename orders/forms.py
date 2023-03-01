from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    # qty = forms.IntegerField(required=True)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
