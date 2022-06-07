from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'บัญชีผู้ใช้ถูกสร้างเรียบร้อยแล้ว')
            return redirect('helpdeskusers:login')
    else:
        form = UserRegisterForm()
    return render(request, 'helpdeskusers/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'บัญชีของคุณอัพเดทเรียบร้อยแล้ว')
            return redirect('helpdeskusers:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'helpdeskusers/profile.html', context)