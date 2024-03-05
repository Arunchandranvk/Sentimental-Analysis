from django import forms
from .models import Contact, FooterContact,Testimonial

class ContactModelForm(forms.ModelForm):

    class Meta:

        model = Contact
        fields = ['username', 'email', 'subject', 'message']

class FeedbackModelForm(forms.ModelForm):

    class Meta:

        model = Testimonial
        fields = ['name', 'position', 'Company', 'text']


class FooterContactModelForm(forms.ModelForm):

    class Meta:

        model = FooterContact
        fields = ['footer_email']