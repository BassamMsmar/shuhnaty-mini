from django.shortcuts import render

from .forms import SingUpForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        user_form = SingUpForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request, 'registration/signup-successful.html', {'user_form':user_form})
    else:
        user_form = SingUpForm()

    return render(request, 'registration/signup.html', {'user_form':user_form})

