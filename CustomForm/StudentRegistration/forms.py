from django import forms
from django.core import validators

# def customValidation(value):
#     if value[0] == '$' or '@':
#         raise forms.ValidationError("Name Should not start with @ or $")


class enroll(forms.Form):
    first_name = forms.CharField(max_length=64, error_messages={'required' : 'Enter Your First Name'})
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField(error_messages={'required': 'Enter your Email'})
    password = forms.CharField(widget=forms.PasswordInput, label="Enter your Password",error_messages={'required' : 'Please Enter Password'})
    rpassword = forms.CharField(widget=forms.PasswordInput, label="Re-Enter your Password",error_messages={'required':'Please Re-Enter your password'})

    error_css_class = 'error'
 

# validation for Paswword:

    def clean(self):
        cleaned_data = super().clean()
        valpwd = cleaned_data.get('password')
        valrpwd = cleaned_data.get('rpassword')
        if valpwd != valrpwd:
            raise forms.ValidationError("Password does not match.")
        if not valpwd:
            raise forms.ValidationError("Please Enter Password.")
        if not valrpwd:
            raise forms.ValidationError("Please Enter Password.")
        

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valpwd = cleaned_data.get('password')
    #     valrpwd = cleaned_data.get('rpassword')

    #     # Check if passwords are provided
    #     if not valpwd:
    #         self.add_error('password', "Please enter a password.")
    #     if not valrpwd:
    #         self.add_error('rpassword', "Please confirm your password.")
        
    #     # Only check for password match if both fields have values
    #     if valpwd and valrpwd and valpwd != valrpwd:
    #         self.add_error('rpassword', "Passwords do not match.")

    #     return cleaned_data