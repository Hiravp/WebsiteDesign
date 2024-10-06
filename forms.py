from django import forms

class PaymentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    phone_number = forms.CharField(label="Phone Number", max_length=15)
    ticket_num = forms.IntegerField(label="Number of Tickets")
    address1 = forms.CharField(label="Address Line 1", max_length=255)
    address2 = forms.CharField(label="Address Line 2", max_length=255, required=False)
    zip_code = forms.CharField(label="ZIP Code", max_length=10)
    country = forms.CharField(label="Country", max_length=50)
    card_num = forms.CharField(label="Card Number", max_length=16)
    expiration = forms.DateField(label="Expiration Date")
    security_code = forms.CharField(label="Security Code", max_length=4)
