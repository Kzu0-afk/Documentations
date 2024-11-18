from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomerSignupForm, UpdateCustomerForm
from .models import Customer

def customer_signup_view(request):
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('customer_entity:signup')
    else:
        form = CustomerSignupForm()
    return render(request, 'customer_entity/signup.html', {'form': form})

def customer_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user and hasattr(user, 'address'):  # Ensure it's a Customer
            login(request, user)
            return redirect('customer_entity:profile')
        else:
            return render(request, 'customer_entity/login.html', {'error': 'Invalid username or password'})

    return render(request, 'customer_entity/login.html')



@login_required
def customer_profile_view(request):
    # Ensure the user is treated as a Customer object
    print(f"Logged in user: {request.user.username}, Email: {request.user.email}")
    customer = get_object_or_404(Customer, id=request.user.id)
    return render(request, 'customer_entity/profile.html', {'customer': customer})


@login_required
def update_customer_profile_view(request):
    customer = get_object_or_404(Customer, id=request.user.id)
    if request.method == 'POST':
        form = UpdateCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_entity:profile')
        else:
            print("Form Errors:", form.errors)  # Debugging
    else:
        form = UpdateCustomerForm(instance=customer)
    return render(request, 'customer_entity/update_profile.html', {'form': form})


@login_required
def customer_delete_account_view(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('customer_entity:signup')
    return render(request, 'customer_entity/delete_account.html')
