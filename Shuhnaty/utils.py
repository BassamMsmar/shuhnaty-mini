from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated :
       return render(request,'')
        
    else:
        return redirect('login')

