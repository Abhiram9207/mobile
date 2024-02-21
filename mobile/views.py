from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View
from mobile.forms import MobileForm,RegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from mobile.models import Mobiles

def signin_required(fn):
     def wrapper(request,*args, **kwargs):
          if not request.user.is_authenticated:
               messages.error(request,"invalid session")
               return redirect("signin")
          else:
               return fn(request,*args, **kwargs)
     return wrapper
@method_decorator(signin_required,name="dispatch")
class MobileListView(View):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        if "brand" in request.GET:
             brand=request.GET.get("brand")
             qs=qs.filter(brand__iexact=brand)
        if "display" in request.GET:
             display=request.GET.get("display")
             qs=qs.filter(display__iexact=display)
        if "price_gt" in request.GET:
             amount=request.GET.get("price_gt")
             qs=qs.filter(price__gte=amount)
        return render(request,"mob_lst.html",{"data":qs})
        
    
# localhost:8000/mobiles/{pk:3}
# @method_decorator(signin_required,name="dispatch")
class MobileDetailView(View):
    def get(self,request,*args,**kwargs):
          # if not request.user.is_authenticated:
          #      return redirect("signin")               
          id=kwargs.get("pk")
          qs=Mobiles.objects.get(id=id)
          return render(request,"mob_details.html",{"data":qs})


        
    
# localhost:8000/mobiles/{id}/remove

class MobileDeleteView(View):

    def get(self,request,*args,**kwargs):
     #    if not request.user.is_authenticated:
     #         return redirect("signin")
        id=kwargs.get("pk")
        Mobiles.objects.get(id=id).delete()
        messages.success(request,"Mobile Delected Sucessfully")
        return redirect("mobile-all")
    

class MobileCreateView(View):
    def get(self,request,*args,**kwargs):
        form=MobileForm()
        return render(request,"mob-add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=MobileForm(request.POST,files=request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"Mobile created sucessfully")
            return redirect("mobile-all")
        
        else:
                    messages.error(request,"mobile created error")
                    return render(request,"mob-add.html",{"form":form})
        


class MobileUpdateView(View):
     def get(self,request,*args,**kwargs):
          id=kwargs.get("pk")
          obj=Mobiles.objects.get(id=id)
          form=MobileForm(instance=obj)
          return render(request,"mobile_edit.html",{"form":form})
     
     def post(self,request,*args,**kwargs):
          id=kwargs.get("pk")
          obj=Mobiles.objects.get(id=id)
          form=MobileForm(request.POST,instance=obj,files=request.FILES)


          if form.is_valid():
               form.save()
               messages.success(request,"Mobile Data Updated Successfully....")
               return redirect("mobile-all")
          else:
               messages.error(request,"can't update mobile data")
               return render(request,"mobile_edit.html",{"form":form})
          
class SignUpView(View):
     def get(self,request,*args,**kwargs):
          form=RegistrationForm()
          return render(request,"register.html",{"form":form})
     
     def post(self,request,*args,**kwargs):
          form=RegistrationForm(request.POST)
          if form.is_valid():

               User.objects.create_user(**form.cleaned_data)
               # form.save

               messages.success(request,"Account created succesfully")
               return render(request,"register.html",{"form":form})
          
          else:
               messages.error(request,"Account creation failed")
               return render(request,"register.html",{"form":form})



class SignInView(View):
     def get(self,request,*args,**kwargs):
          form=LoginForm()
          return render(request,"login.html",{"form":form})
     
     def post(self,request,*args,**kwargs):
          form=LoginForm(request.POST)

          if form.is_valid():
               uname=form.cleaned_data.get("username")
               pwd=form.cleaned_data.get("password")
               print(uname,pwd)
               user_object=authenticate(request,username=uname,password=pwd)
               if user_object:
                    print("valid credentials")
                    login(request,user_object)
                    print(request.user)
                    return redirect("mobile-all")
               else:
                    print("invalid credentials")
               return render(request,"login.html",{"form":form})
          else:
               return render(request,"login.html",{"form":form})



class SignOutView(View):
     def get(self,request,*args,**kwargs):
          logout(request)
          return redirect("signin")    



