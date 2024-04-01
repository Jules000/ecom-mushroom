from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Your name"
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': "Your e-mail"
    }))
    telephone= forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'placeholder': "Your cellphone number"
    }))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Your message's subject"
    }))
    message = forms.CharField( widget=forms.Textarea(attrs={
        'placeholder': "Your message"
    }))