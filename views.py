from django.shortcuts import render
from .forms import PaymentForm  # Assuming the form is in forms.py

def payment_form_view(request):
    # Handle POST request
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to the database)
            # form.cleaned_data['name'], etc.
            pass
    else:
        # Create an empty form instance for GET requests
        form = PaymentForm()

    # Render the template and pass the form
    return render(request, 'payment_form.html', {'form': form})




""" 
Things that DEFINETLY need editing

1) Styling on form (hopefully Soham figures it out)
2) Styling and functionality of thank you page (payments/thank-you)

Things that might need editing

3) URL names defined in views (/thank-you)
4) File names (reviews/post_submission.html & reviews/transactions.html)

How to edit aforementioned things

1) Add styling for it ig idk how that works
2) Functionality can be defined by Hirav or it can be deleted alltogether & go back to home; Soham can do styling
3) Use a url name defined earlier by Hirav in his part of the project instead of thank-you
4) Just edit the file structure as needed idk

Special note

5) Ik i kind of suck at this so ill make a google form if this code doesn't work out (it worked in testing tho)

"""