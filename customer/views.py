from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView
from django.contrib.auth.models import User
from .forms import UserUploadsForm,UserInviteForm,PropicForm
from django.utils.decorators import method_decorator
from account.views import decs,SignUpForm
from.models import UserUploads,TravelInvites,Profilepictures,Room,Message
from django.contrib import messages
from django.contrib.auth import logout
from .forms import *
from django.utils.text import slugify

@method_decorator(decs,name='dispatch')
class UserView(View):
    def get(self,request):
        form=UserInviteForm()
        # lists=TravelInvites.objects.all()
        lists=Room.objects.all()
        return render(request,'userhome.html',{'f':form,'li':lists})
    def post(self,request):
        fdata=UserInviteForm(data=request.POST)
        if fdata.is_valid():
            fdata.instance.user=self.request.user
            instances=fdata.save()            
            room_name = f"{instances.Destination} - {instances.Location}"
            room_slug = slugify(room_name)
            Room.objects.create(invite=instances,name=room_name,slug=room_slug)
            return redirect('userhome')
        return render(request,"userhome.html")

# class RoomView(TemplateView):
#     template_name="room.html"  
class RoomView(View):
    def get(self,request,*args,**kwargs):
        slug=kwargs.get('slug')
        room = Room.objects.get(slug=slug)
        messages = Message.objects.filter(room=room)[0:25]
        return render(request, 'room.html', {'room': room, 'messages': messages})

@method_decorator(decs,name='dispatch')    
class Proview(View):
    def get(self,request):
        form=UserUploadsForm()
        propic=PropicForm()
        pic=Profilepictures.objects.filter(user=self.request.user).first()
        print(pic)
        ti=TravelInvites.objects.filter(user=self.request.user)
        img=UserUploads.objects.filter(user=self.request.user)
        return render(request,"profile.html",{'f':form,'form':ti,'img':img,'pp':propic,'p':pic})
    def post(self,request):
        form_data=UserUploadsForm(data=request.POST,files=request.FILES)
        fdata=PropicForm(data=request.POST,files=request.FILES)
        if fdata.is_valid():
            fdata.instance.user=self.request.user
            fdata.save()
            return redirect('profile')
        if form_data.is_valid():
            form_data.instance.user=self.request.user
            form_data.save()
            messages.success(self.request,"Updated Successfully")
            return redirect('profile')
        return render(request,"profile.html")

@method_decorator(decs,name='dispatch')
class Editprofile(View):
    def get(self,request):
        res=self.request.user
        print(res)
        form=ProfileForm(instance=res)
        propic=Profilepictures.objects.filter(user=res).first()
        form1=PropicForm(instance=propic)
        return render(request,"editprofile.html",{'form':form,'form1':form1})
    def post(self,request):
        res=self.request.user
        res1=Profilepictures.objects.filter(user=res).first()
        form_data=ProfileForm(data=request.POST,instance=res,files=request.FILES)
        fdata=PropicForm(data=request.POST,instance=res1,files=request.FILES)
        if fdata.is_valid():
            # fdata.instance=self.request.user
            # print(fdata)
            instance=fdata.save(commit=False)
            instance.user=self.request.user
            instance.save()
        if form_data.is_valid():
            # form_data.instance=self.request.user
            form_data.save()
            # print(form_data)
            messages.success(self.request,"Update Successful!!")
            return redirect('profile')
        # messages.error(self.request,"Error")
        return render(request,"profile.html")
    
class Delview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        inv=TravelInvites.objects.get(id=id)
        inv.delete()
        messages.success(self.request,"Deleted")
        return redirect('profile')

class Delpro(View):
    def get(self,request,**kwargs):
        id=kwargs.get('id')
        user=User.objects.get(id=id)
        user.delete()
        messages.success(self.request,"Deleted")
        logout(request)
        return redirect('signup')

class DelPic(View):
    def get(self,request,**kwargs):
        id=kwargs.get('id')
        inv=UserUploads.objects.get(id=id)
        inv.delete()
        messages.success(self.request,"Deleted")
        return redirect('profile')

    
# class ChatView(View):
#     def get(self,request,*args,**kwargs):
#         slug=kwargs.get('slug')
#         room= Room.objects.get(slug=slug)
#         messages=Message.objects.filter(room=room)[0:25]
#         return render(request,'userhome.html',{'room':room,'messages':messages})
        