from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def login_view(request):
    # if request.method == 'POST' :
    #     un,pw = request.POST.get('username'),request.POST.get('password')
    #     print(un,pw)
    #     user = authenticate(request,username=un,password=pw)
    #     if user is None :
    #         return render(request,'accounts/login.html',{'err':'Invalid UN/PW'})   
    #     login(request,user)
    #     return redirect('/')
    # return render(request,'accounts/login.html')

    if request.method == 'POST' :
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid() :
            user = form.get_user()
            login(request,user)
            return redirect('/')
    else:  
        form = AuthenticationForm(request)
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST' :
        logout(request)
        return redirect('/login')
    return render(request,'accounts/logout.html')

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid() :
        user_obj = form.save()
        return redirect('/login')
    return render(request,'accounts/register.html',{'form':form})