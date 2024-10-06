from django.shortcuts import render, redirect
from .forms import customer_info
from django.http import HttpResponseRedirect

def customer_info_view(request):
    if request.method == 'POST':
        form = customer_info(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return redirect("thank_you")  # Redirect to thank you page after its defined ig
        else:
            form = customer_info()  # For GET request, display an empty form

    else:
        form = customer_info()
        
    return render(request, 'reviews/transactions.html', 
        {'form': form}) # defines form as form template

def thank_you(request):
    return render(request, "reviews/post_submission.html")

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