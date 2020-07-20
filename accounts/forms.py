from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Order


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation", 
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm you password")

        if password1 != password2:
            raise ValidationError("Passwords must match")

        return password2


    class MakePaymentForm(forms.Form):
        MONTH_CHOICES = [(i, i) for i in range(1, 12)]
        YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

        credit_card_number = forms.CharField(label='Credit card number', required=False)

        cvv = forms.CharField(label='Security code (CVV)', required=False)

        expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)

        expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)

        stripe_id = forms.CharField(widget=forms.HiddenInput)

        same_billing_address = forms.BooleanField(required=False, label="Billing address is the same as my shipping address")

        set_default_shipping = forms.BooleanField(required=False, label="Save as default shipping address")


class BillingForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'county'
        )


class ShippingForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'county'
        )