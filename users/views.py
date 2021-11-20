from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import JsonResponse
from actions.models import Action


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        request.session['username'] = user.username
        request.session['role'] = user.profile.role
        messages.add_message(request, messages.SUCCESS, "Welcome: %s" % user.username)
        return redirect('food_critics:home')
    else:
        return render(request,
                  "users/user/register.html")

#login view
def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    try:
        user = authenticate(username=username, password=password)
        if(user is not None):
            request.session['username'] = user.username
            request.session['role'] = user.profile.role
            messages.add_message(request, messages.SUCCESS, "Welcome %s" % user.get_username())
            return redirect('food_critics:blog-list')
        else:
            messages.add_message(request, messages.ERROR, "Did you change your password recently?")
            return redirect('food_critics:home')
    except:
        messages.add_message(request, messages.ERROR, "There was no user! Try signing up")
        return redirect('food_critics:home')
    
#logout view
def logout(request):
    request.session['username'] = ''
    request.session['role'] = ''
    del request.session['username']
    del request.session['role']
    messages.add_message(request, messages.SUCCESS, "Successfully logged out!")
    return redirect('food_critics:home')

def user_profile(request,username):
    user = User.objects.get(username=username)
    return render(request,'users/user/profile.html',{"user":user})

def user_points(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            return JsonResponse({"success":"success", 'username':user.username, 'points':user.points },status=200)
        except User.DoesNotExist:
            return JsonResponse({"error":"User not found with that name"},status=200)
    else:
        return JsonResponse({"error":"Invalid Ajax Request"},status=400)

#update Profile
def update_profile(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == 'POST':
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobileno = request.POST.get('mobileno')
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.email = email
            user.profile.mobileno = mobileno
            user.save()

            #save Action
            action = Action(user=user, verb='created profile', target=user)
            action.save()

            request.session['username'] = user.username 
            messages.add_message(request, messages.SUCCESS, "Successfully updated Profile")
            return JsonResponse({"success":"success"},status=200)
        except:
            messages.add_message(request, messages.ERROR, "There was no user! Try signing up")
            return JsonResponse({"error":"User not found with that name"},status=200)
    else:
        return JsonResponse({"error":"Invalid Ajax Request"},status=400)