from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from allauth.account.forms import LoginForm
from allauth.account.views import SignupView
from .forms import ProfileForm, CustomSignupForm

class CustomSignupView(SignupView):
    template_name = 'account/signup.html'
    form_class = CustomSignupForm

    def form_valid(self, form):
        user = form.save(self.request)
        return redirect('signup_complete')

def landing(request):
    return render(request, 'landing.html', {'login_form': LoginForm()})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})

def signup_complete(request):
    return render(request, 'account/signup_complete.html')



