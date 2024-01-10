from django.shortcuts import render 
from authapp.models import Members


# Create your views here.

def home_page(request):
    return render(request,  'index.html')

def login_page(request):
    context = {}

    if request.method == 'POST':
        username_sent = request.POST.get('uname')
        if Members.check_user_exist(Members, username_sent):
            posted_info = {
                'username': username_sent,
                'password': request.POST.get('password')
            }
            if Members.login_user(Members, posted_info):
                msg = 'you have been loged in'
            else :
                msg = 'login failed'
        context['login_msg'] = msg

    return render(request, 'login.html',  context)


def register_page(request):
    context = {'registration_msg': ''}
    if request.method == 'POST':
        
        print(request.POST.get('uname'))
        posted_info  = {
            'username': request.POST.get('uname'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password')
        }
        if Members.is_valid(Members, posted_info=posted_info):
            Members.register_user(Members)
            registration_msg = 'registration complete!!'
        else :
             registration_msg = 'invalid email or username'
        
        context = {
            'registration_msg': registration_msg,
        }    
    return render(request, 'register.html', context)