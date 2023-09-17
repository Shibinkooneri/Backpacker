from django.shortcuts import render,redirect
from .forms import SignUpForm,SignInForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import View,CreateView,FormView
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache



def Signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"Please login First")
            return redirect('signin')
    return inner
decs=[Signin_required,never_cache]


def HomeView(request):
    return render(request,"Home.html")

class SignUpView(CreateView):
    form_class=SignUpForm
    template_name="signup.html"
    success_url=reverse_lazy("signin")
    def form_valid(self,form):
        messages.success(self.request,"Registration Successful!!")
        return super().form_valid(form)

class SignInView(FormView):
    template_name="signin.html"
    form_class=SignInForm
    def post(self,request):
        fdata=SignInForm(data=request.POST)
        if fdata.is_valid():
            unam=fdata.cleaned_data.get("username")
            pswd=fdata.cleaned_data.get("password")
            user=authenticate(request,username=unam,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"Login Successful!!!")
                return redirect('userhome')
            else:
                messages.error(request,"Login Failed!! Invalid Username or Password!!")
                return redirect('signin')
        return render(request,'signin.html',{"form":fdata})
        
class Lgout(View):
    def get(self,request):
        logout(request)
        return redirect("home")