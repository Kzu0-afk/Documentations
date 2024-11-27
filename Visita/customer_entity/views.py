from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Hotel
from user_entity.backends import CustomerBackend
from .forms import CustomerSignupForm, UpdateCustomerForm
from .models import Customer
from django.contrib.auth import get_backends

def customer_landing_page(request):
    hotels = Hotel.objects.all()  # Fetch all hotels
    return render(request, 'customer_entity/customer_landing.html', {'hotels':hotels})

def customer_signup_view(request):
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('customer_entity:login')  # Redirect to profile
    else:
        form = CustomerSignupForm()
    return render(request, 'customer_entity/signup.html', {'form': form})


def customer_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        # Check if the user is authenticated and is a Customer
        if user is not None:
            try:
                customer = Customer.objects.get(id=user.id)  # Check if the user is a Customer
                login(request, user)  # Log the user in
                return redirect('customer_entity:landing_page')
            except Customer.DoesNotExist:
                return render(request, 'customer_entity/login.html', {'error': 'Invalid user type.'})
        else:
            return render(request, 'customer_entity/login.html', {'error': 'Invalid username or password.'})

    return render(request, 'customer_entity/login.html')

@login_required
def customer_profile_view(request):
    # Ensure the user is treated as a Customer object
    customer = get_object_or_404(Customer, id=request.user.id)
    return render(request, 'customer_entity/profile.html', {'customer': customer})

@login_required
def update_customer_profile_view(request):
    customer = get_object_or_404(Customer, id=request.user.id)
    if request.method == 'POST':
        form = UpdateCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            user = form.save(commit=False)

            # Validate using the backend
            backend = CustomerBackend()
            authenticated_user = backend.get_user(user.id)

            if authenticated_user:
                # Save the user only if authenticated
                user.save()
                return redirect('customer_entity:profile')
            else:
                # Handle invalid backend authentication
                form.add_error(None, "Authentication failed during profile update.")
    else:
        form = UpdateCustomerForm(instance=customer)
    return render(request, 'customer_entity/edit_profile.html', {'form': form})

@login_required
def customer_delete_account_view(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('customer_entity:signup')
    return render(request, 'customer_entity/delete_account.html')

@login_required
def customer_logout_view(request):
    logout(request)  # Log out the user
    return redirect('customer_entity:login')  # Redirect to the customer login page

@login_required
def customer_landing_page(request):
    hotels = Hotel.objects.all() #Fetch all hotels
    return render(request, 'customer_entity/customer_landing.html', {'hotels':hotels})