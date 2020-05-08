from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have logged in successfuly.')
            return redirect('dashboard')
        else:
            messages.error(
                request, 'Please make sure your username and pass is correct!!!')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password2 = request.POST['password2']
        password = request.POST['password']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken!!!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, 'This email is already registered!!!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name,
                                                    last_name=last_name,
                                                    username=username,
                                                    email=email,
                                                    password=password)
                    # auth.login(request, user)
                    # messages.success(request, ' you have registered successfully.')
                    # return redirect(request, 'index')
                    user.save()
                    messages.success(
                        request, 'you have registered successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match!!!')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.filter(
        user_id=request.user.id).order_by('-contact_time')
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
