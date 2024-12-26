from django.shortcuts import render
from . models import NameForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.shortcuts import render
from .models import NameForm, AddMoney

def home(request):
    formname = NameForm.objects.get(id=1)
    
    money = None
    if request.user.is_authenticated:
        try:
            money = AddMoney.objects.get(user=request.user)
        except AddMoney.DoesNotExist:
            money = None
    
    return render(request, 'home.html', {'money': money, 'formname': formname})

    
from django.shortcuts import render, redirect
from .models import *
from .form import *



@login_required
def Cform(request):
    if request.method == 'POST':
             Channel_Name = request.POST["ChannelName"]
             Channel_Url = request.POST["ChannelUrl"]
             Channel_Id = request.POST["ChannelId"]
             Channel_Description = request.POST["message"]
             print(Channel_Name)
          
             f = YoutubeChannel(
                   channel_name=Channel_Name,
                   channel_url=Channel_Url,
                   channel_id=Channel_Id,
                   description=Channel_Description,
                   statue = "Pending"
               )
             f.save()
             
             return redirect('formSubmit')  # Replace 'success_url' with the actual URL or name of the success page
           
    
      
    return render(request, 'form.html')

    
@login_required
def formsee(request):
    form = YoutubeChannel.objects.filter(user=request.user)
    formname = NameForm.objects.get(id=1)
    return render(request,'yourForm.html',{'form':form})


class CustomerRegistrationView(View):
  def get(self,request):
     form = CustomerRegistrationForm()
     return render(request, 'customerregistration.html', {'form':form})
  
  def post(self,request):
     form = CustomerRegistrationForm(request.POST)
     if form.is_valid():
        messages.success(request,'Congratulations registration done.')
        form.save()
     return render(request, 'customerregistration.html', {'form':form})


def profile(request):
    return render(request,'profile.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer


@login_required
def profile(request):
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        customer = Customer(user=request.user)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'profile.html', {'form': form})