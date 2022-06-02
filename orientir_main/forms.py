from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    name = forms.CharField(label='Имя', required=True)
    mess = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)
