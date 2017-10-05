from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# The login page at the "start" of the website
@csrf_protect
def enter(request):
    return render(request, 'core/login.html')

# If a valid username and password are not provided, the user is prompted to provide them
# Otherwise they are redirected to the homepage
@csrf_protect
def login_error(request):
    try:
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
    except:
        user = None

    if user is not None:
        login(request,user)
        return redirect(home)
    else:
        return render(request, 'core/login.html', {'warning': 'Please provide a valid username and password'})


# The homepage of a logged in user. If the user is not logged in, the decorator redirects them to the login page
@requires_csrf_token
@login_required(login_url='/')
def home(request):
    return render(request, 'core/home.html', {'content': 'Lorem ipsum'*50})

# Logs out the user. On log out requests on the site, the user is redirected to "/logout/" which triggers this view
def logout_view(request):
    logout(request)
    return redirect('/')