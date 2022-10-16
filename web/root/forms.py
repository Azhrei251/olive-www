from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Name"
    }))
    email = forms.EmailField(required=True, label=False, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': "Email"
    }))
    message = forms.CharField(required=True, label=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': "Message"
    }))
