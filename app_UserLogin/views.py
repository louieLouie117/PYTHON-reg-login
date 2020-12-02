from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt



# Create your views here.
#urls paths----------------------------------------------------------
def login_user(request):
    #sending to dashboard
    print(request.POST)
    #check if the email is in the db
    users_list = User.objects.filter(user_email= request.POST['user_email'])
    if len(users_list) == 0:
        return redirect('/')
    
    #check if the password matches
    if bcrypt.checkpw(request.POST['user_password'].encode(),users_list[0].user_password.encode()):
        #set user in session
        request.session['uuid'] = users_list[0].id
        print(users_list[0].user_password)
        return redirect('/success')


   

def logout(request):
    #send to index
    request.session.flush()
    return redirect('/')



#pages----------------------------------------------------------------
def index(request):
    return render(request, 'index.html')

def show_dashboard(request):
    #check if user is not in session
    if 'uuid' not in request.session:
        return redirect('/')
    context = {
        'user_name': User.objects.get(id=request.session['uuid']).first_name
    }
    return render(request, 'dashboard.html', context)


#from actions-----------------------------------------------------------
def register_user(request):
    #erros
    errors = User.objects.register_validator(request.POST)
    print("erros found****", errors)

    if len(errors) > 0:
        # if the errors dictionary contains anything,
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        print(key)
        return redirect('/')
    else:
        #hash the password
        hash_browns = bcrypt.hashpw(request.POST['user_password'].encode(),
        bcrypt.gensalt()).decode()
        print('hassing', hash_browns)

        #create user
        print("User was added",request.POST)
        created_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            user_email = request.POST['user_email'],
            # user_password = request.POST['user_password'],replace with hash
            user_password = hash_browns

        )
        print('hash borwns',created_user.user_password)

        #set user in seesion
        request.session['uuid'] = created_user.id
    
        return redirect('/success')


    

