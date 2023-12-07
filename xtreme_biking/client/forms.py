from django import forms
from .models import CustomerShipping, CustomerPaymentMethod, Customer
from accounts.models import CustomUser


class PaymentMethodForm(forms.ModelForm):
    payment_info = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = CustomerPaymentMethod
        fields = ['method']

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super(PaymentMethodForm, self).__init__(*args, **kwargs)
        if user_id is not None:
            user = CustomUser.objects.filter(id=user_id)
            self.fields['customer'].queryset = Customer.objects.filter(
                user=user)


class ShippingAdressForm(forms.ModelForm):
    shipping_info = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = CustomerShipping
        fields = ['address', 'city', 'state', 'zipcode']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ShippingAdressForm, self).__init__(*args, **kwargs)
        if user:
            self.initial['customer'] = user.customer

