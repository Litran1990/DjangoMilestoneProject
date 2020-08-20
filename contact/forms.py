from django import forms


class ContactForm(forms.Form):

    email = forms.EmailField(required=True)
    reason = forms.CharField(max_length=50, required=True)
    description = forms.CharField(widget=forms.Textarea, max_length=500, required=True)