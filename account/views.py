from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = AddUsersForm(request.POST)
        if form.is_valid():
            # Create a new user but don't save it yet
            new_user = form.save(commit=False)

            # Save the user to the database
            new_user.save()
      
            request.session['registeration'] = True
            request.session['redirect_url'] = reverse('articles_list')
            
            # Redirect to a success message page
            return HttpResponseRedirect(reverse('success_message_view'))
    else:
        form = AddUsersForm()

    return render(request, 'account/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the given username exists
        try:
            logged_user = CustomUser.objects.get(username=username, password=password)
        except CustomUser.DoesNotExist:
            return render(request, 'account/login.html', {'error_message': 'Invalid credentials'})
        
        if logged_user:
            login(request, logged_user)
            #print('logged in ', request.user.username)
        else:
            return render(request, 'account/login.html', {'error_message': 'Invalid credentials'})
        # Redirect to a dashboard or another page after successful login
        return redirect('articles_list')
     
    return render(request, 'account/login.html')


def success_message_view(request):
    if request.session.get('registeration', False):
        redirect_url = request.session.get('redirect_url')
        
        # Clear session variables
        request.session.pop('registeration', None)
        request.session.pop('redirect_url', None)

        return render(request, 'account/success_message.html', {'success_message':  "User registered successfully", 'redirect_url': redirect_url})
    else:
        return JsonResponse({'status':'fail', 'message':'Forbidden request', 'status_code':403}, status=403)


@login_required
def user_logout(request):
    # Log the user out
    if request.user.is_authenticated:
        # logout(request)
        # return JsonResponse({'message':'logout_success'})
        # Set the logout message
        logout_message = f"{request.user.username} !! You have been successfully logged out."

        # Log the user out
        logout(request)

        # Render the logout message template
        return render(request, 'account/logout_message.html', {'logout_message': logout_message})
    else:
        return redirect('user_login')  # Redirect to login page if user is not logged in
    
@login_required  
def view_user_profile(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(id=request.user.id)
        context = {'user': user}
        return render(request, 'account/user_profile.html', context)