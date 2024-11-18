from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import AdminSignupForm, UpdateAdminForm
from .models import AdminEntity

def admin_signup_view(request):
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('admin_entity:profile')
    else:
        form = AdminSignupForm()
    return render(request, 'admin_entity/signup.html', {'form': form})

def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user and hasattr(user, 'departmentRole'):  # Ensure it's an Admin
            login(request, user)
            return redirect('admin_entity:profile')
        else:
            return render(request, 'admin_entity/login.html', {'error': 'Invalid username or password'})

    return render(request, 'admin_entity/login.html')



@login_required
def admin_profile_view(request):
    print(f"Logged in user: {request.user.username}, Email: {request.user.email}")
    admin = get_object_or_404(AdminEntity, id=request.user.id)
    return render(request, 'admin_entity/profile.html', {'admin': admin})

@login_required
def update_admin_profile_view(request):
    admin = get_object_or_404(AdminEntity, id=request.user.id)
    if request.method == 'POST':
        form = UpdateAdminForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            return redirect('admin_entity:profile')
        else:
            print("Form Errors:", form.errors)  # Debugging
    else:
        form = UpdateAdminForm(instance=admin)
    return render(request, 'admin_entity/update_profile.html', {'form': form})


@login_required
def admin_delete_account_view(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('admin_entity:signup')
    return render(request, 'admin_entity/delete_account.html')
