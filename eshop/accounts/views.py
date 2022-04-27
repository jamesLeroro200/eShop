from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

User = get_user_model()

# Create your views here.
def signUp(request):
    if request.method == 'POST':
        #Traitement du formulaire: Inscription_utilisateur
        username = request.POST.get('user-name')
        email = request.POST.get('email-address')
        password = request.POST.get('password')
        User.objects.create_user(username=username,
                                        password=password,
                                        email=email)
        return redirect('signin')

    return render(request, 'accounts/signUp.html')

def signIn(request):
    if request.method == 'POST':
        #Traitement du formulaire: Connexion_utilisateur
        username = request.POST.get('user-name')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('index')

    return render(request, 'accounts/signIn.html')

def logout_user(request):
    logout(request)
    return redirect('index')
