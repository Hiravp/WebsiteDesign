from django import forms
from django.core.validators import RegexValidator

def num_only():
    return [RegexValidator(r'^\d+$', 'Please enter a valid number.')]


class customer_info(forms.Form):
    name = forms.CharField(label="Full name (as written on your card)", max_length=100, error_messages={
                           "required": "This field is required"})
    
    email = forms.EmailField(label='Email Address', max_length=75, min_length=6, error_messages={
                           "required": "This field is required",
                           "min_length": "Please enter a valid email address"})
    
    phone_number = forms.CharField(label='Phone number', max_length=10, min_length=10, validators=num_only(), error_messages={
                           "required": "This field is required",
                           "min_length": "Please enter a 10 digit phone number (people outside the US cannot book tickets)"})
    
    ticket_num = forms.ChoiceField(label='How many tickets would you like to book', choices=[(i, int(i)) for i in range(1, 11)], error_messages={
        "required": "This field is required",
        "max_value": "You can only purchase a maximum of 10 tickets"})
    
    address1 = forms.CharField(label='Address 1 (required)', max_length=100, error_messages={
                           "required": "This field is required"})
    
    address2 = forms.CharField(label='Address 2 (optional)', max_length=100, required=False)
    
    zip_code = forms.CharField(label='Zip code (5 digits)', max_length=5, validators=num_only(), error_messages={
                           "required": "This field is required"})
    
    country = forms.CharField(label='Country', max_length=50, error_messages={
                           "required": "This field is required"})
    
    card_num = forms.CharField(label='16 digit card number', max_length=16, validators=num_only(), error_messages={
                           "required": "This field is required"})
    
    expiration = forms.CharField(label='Expiration date (MM/YY)', max_length=5, error_messages={
                           "required": "This field is required"})
    
    security_code = forms.CharField(label='3 or 4 digit security code', max_length=4, validators=num_only(), error_messages={
                           "required": "This field is required"})

# Change the text right of "required": inside quotation marks if needed
