from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,  request.FILES)
        if form.is_valid():
            print("Archivos recibidos:", request.FILES)
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.bio = form.cleaned_data['bio']
            user.avatar = form.cleaned_data['avatar']

            user.save()
            return redirect('login')
        else:
            print("Errores del formulario:", form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def custom_logout(request):
    logout(request)
    return redirect('/')