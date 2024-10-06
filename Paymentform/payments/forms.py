from django import forms

class customer_info(forms.Form):
    name = forms.CharField(label='Full name (as it appears on your card)', max_length=100, error_messages={
                           "required": "This field is required"})
    email = forms.EmailField(label='Your Email Address', max_length=75, error_messages={
                           "required": "This field is required"})
    phone_number = forms.IntegerField(label='Phone number', max_value=9999999999, error_messages={
                           "required": "This field is required"})
    address1 = forms.CharField(label='Address 1 (required)', max_length=100, error_messages={
                           "required": "This field is required"})
    address2 = forms.CharField(label='Address 2 (optional)', max_length=100)
    zip_code = forms.IntegerField(label='Zip code (5 digits)', max_value=99999, error_messages={
                           "required": "This field is required"})
    country = forms.CharField(label='Country', max_length=50, error_messages={
                           "required": "This field is required"})
    card_num = forms.CharField(label='16 digit card number', max_length=16, error_messages={
                           "required": "This field is required"})
    expiration = forms.CharField(label='Expiration date (MM/YY)', max_length=5, error_messages={
                           "required": "This field is required"})
    security_code = forms.CharField(label='3 or 4 digit security code', max_length=4, error_messages={
                           "required": "This field is required"})

# Change the text right of "required": inside quotation marks if needed
