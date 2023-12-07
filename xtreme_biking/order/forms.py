from django import forms
from client.models import CustomerShipping, CustomerPaymentMethod, Customer
from accounts.models import CustomUser
from .models import CustomerReviews, CustomerClaims

class reviewForm(forms.ModelForm):
    review_info = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = CustomerReviews
        fields = ['review']

    def __init__(self, *args, **kwargs):
        order = kwargs.pop('order', None)
        super(reviewForm, self).__init__(*args, **kwargs)
        if order:
            self.initial['order'] = order

class claimForm(forms.ModelForm):
    claim_info = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = CustomerClaims
        fields = ['claim']

    def __init__(self, *args, **kwargs):
        order = kwargs.pop('order', None)
        super(claimForm, self).__init__(*args, **kwargs)
        if order:
            self.initial['order'] = order