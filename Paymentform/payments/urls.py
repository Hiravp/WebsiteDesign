from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name='home'),
    path("transactions/", views.customer_info_view, name='transaction_form'),
    path("thank-you/", views.thank_you, name='thank_you'),
    path("seating/", views.seating),
    path("calendar/", views.calendar)
]

"""
Things that might need changing

1) Change name of second url path from thank-you to something else (just don't edit views.thank_you since thats the function name in views.py nobody will see it)
"""