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
            login(request, user)  # Log the user in after signup
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

            # Update password only if provided
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])

            user.save()
            login(request, user)  # Re-log the user after password change
            return redirect('customer_entity:profile')
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
    return render(request, 'customer_entity/customer_landing.html')