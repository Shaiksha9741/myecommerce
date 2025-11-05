from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import TokenGenerator, generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate, login, logout


def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password != confirm_password:
            messages.warning(request, "Passwords do not match")
            return render(request,'authentication/signup.html')
        try:
            if User.objects.get(username=email):
                messages.info(request, "Email is taken")
                # return HttpResponse("User already exists")
            return render(request,'authentication/signup.html')
        except Exception as indentifier:
            pass
        user = User.objects.create_user(email,email,password)
        user.is_active = False
        user.save()
        email_subject="Activate Your Account"
        message=render_to_string('authentication/activate_email.html', {
            'user': user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user),   
        })
        
        email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [email])
        email_message.send()
        messages.success(request, "Account created successfully, please check your email to activate your account")
        return redirect('handlelogin')  # Redirect to login page after signup
    return render(request, 'authentication/signup.html')
 
class ActivateAccountView(View):
    def get(self, request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as indentifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active = True
            user.save()
            messages.info(request, "Account activated successfully")
            return redirect('handlelogin')
        return render (request, 'authentication/activate_failed.html')



def handlelogin(request):
    if request.method == "POST":
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username, password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request, "Login successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect('handlelogin')
    return render(request, 'authentication/login.html')
    




def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('handlelogin')