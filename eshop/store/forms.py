from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea({'rows': 3}),
                              help_text='You can leave us a message and we will get back to you as soon as possible.')
    sender = forms.EmailField()