# here we are implementing form validation
# 1.) custom validation - by writing our own function
# 2.) Django's Inbuilt validators - by importing and using validators on field which we want to validate.

from django import forms
from django.core import validators


# below is the custom form validator method
# Custom validator-1

# custom validator for name which will ensure name is started with character 's'

# def check_for_s(value):
#     if value[0].lower() != 's':
#         raise forms.ValidationError("Name needs to be starts with s")


class FormName(forms.Form):

    #name = forms.CharField(validators=[check_for_s])    uncomment this line if you want to use our above custom validator on name

    name = forms.CharField()

    # email = forms.EmailField(validators=[validators.MaxLengthValidator(30)]) # inbuilt validator to keep the length of the email upto 30 characters.

    email = forms.EmailField()

    verify_email = forms.EmailField(label="verify email");

    text = forms.CharField(widget=forms.Textarea)

    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])

    #Custom validator-2

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("Gotcha Bot !")
    #     return botcatcher

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email!=vmail:
            raise forms.ValidationError("make sure email matches !")
