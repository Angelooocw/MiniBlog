from django import forms

# models
from .models import Subscribers, Contact


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo electronico...',
                    'class': 'input-email'
                }
            )
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')
