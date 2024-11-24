from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, get_backends
from django.contrib.auth.decorators import login_required
from user_entity.backends import AdminBackend
from .forms import AdminSignupForm, UpdateAdminForm
from .models import AdminEntity
# Create your views here.

def admin_home(request):
    return HttpResponse("Admin home page")

def admin_dashboard(request):
    # You can pass context if needed
    return render(request, 'admin_entity/admin_dashboard.html')


def admin_signup_view(request):
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('admin_entity:profile')  # Redirect to profile
    else:
        form = AdminSignupForm()
    return render(request, 'admin_entity/signup.html', {'form': form})


def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(f"Username: {username}, Authenticated user: {user}")

        # Check if the user is authenticated and is an AdminEntity
        if user is not None:
            try:
                admin = AdminEntity.objects.get(id=user.id)  # Check if the user is an Admin
                login(request, user)  # Log the user in
                return redirect('admin_entity:admin-dashboard')
            except AdminEntity.DoesNotExist:
                return render(request, 'admin_entity/login.html', {'error': 'Invalid user type.'})
        else:
            return render(request, 'admin_entity/login.html', {'error': 'Invalid username or password.'})

    return render(request, 'admin_entity/login.html')


@login_required
def admin_profile_view(request):
    admin = get_object_or_404(AdminEntity, id=request.user.id)
    return render(request, 'admin_entity/profile.html', {'admin': admin})


@login_required
def update_admin_profile_view(request):
    admin = get_object_or_404(AdminEntity, id=request.user.id)
    if request.method == 'POST':
        form = UpdateAdminForm(request.POST, instance=admin)
        if form.is_valid():
            user = form.save(commit=False)

            # Update password only if provided
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])

            user.save()

            # Explicitly set the backend for the admin
            backends = get_backends()
            for backend in backends:
                if isinstance(backend, AdminBackend):
                    user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
                    break

            login(request, user)  # Re-log the user after password change
            return redirect('admin_entity:profile')
    else:
        form = UpdateAdminForm(instance=admin)
    return render(request, 'admin_entity/edit_profile.html', {'form': form})




@login_required
def admin_delete_account_view(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('admin_entity:signup')
    return render(request, 'admin_entity/delete_account.html')

@login_required
def admin_logout_view(request):
    logout(request)  # Log out the user
    return redirect('admin_entity:login')  # Redirect to the admin login page

