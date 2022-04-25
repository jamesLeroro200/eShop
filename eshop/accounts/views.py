from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def signUp(request):
    if request.method == 'POST':
        #Traitement du formulaire
        username = request.POST.get('user-name')
        email = request.POST.get('email-address')
        password = request.POST.get('password')
        User= User.objects.create_user(username=username,
                                        password=password,
                                        email=email)
        return redirect('index')

    return render(request, 'accounts/signUp.html')
