from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import FormView,TemplateView,CreateView
from .forms import *
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
# Create your views here

class LoginView(FormView):
    template_name="login.html"
    form_class=LogForm
    def post(self,request,*args,**kwargs):
        log_form=LogForm(data=request.POST)
        if log_form.is_valid():  
            us=log_form.cleaned_data.get('username')
            ps=log_form.cleaned_data.get('password')
            user=authenticate(request,username=us,password=ps)
            if user: 
                login(request,user)
                if request.user.is_superuser == True:
                   return redirect('h')
            else:
                return render(request,'login.html',{"form":log_form})
        else:
            return render(request,'login.html',{"form":log_form}) 


# class HomeView(TemplateView):
#     template_name = "home.html"


from main.models import Header, Home, Callback, Title, Service, Info, Count, About, Testimonial, Contact, Sponsor, FooterContact
from main.forms import ContactModelForm, FooterContactModelForm

# Create your views here.

def indexadmin(request):
    header = Header.objects.first()
    home = Home.objects.all()
    callback = Callback.objects.first()
    titles = Title.objects.first()
    services = Service.objects.all()
    info = Info.objects.first()
    count = Count.objects.all()
    about = About.objects.first()
    testimonials = Testimonial.objects.all()
    sponsors = Sponsor.objects.all()

    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        form2 = FooterContactModelForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('/')
        if form2.is_valid():
            FooterContact.objects.create(**form2.cleaned_data)
            return redirect('/')
    else:
        form = ContactModelForm()

    return render(request, 'home.html', context={
        'header':header,
        'home':home,
        'callback':callback,
        'titles':titles,
        'services':services,
        'info':info,
        'count':count,
        'about':about,
        'testimonials':testimonials,
        'sponsors':sponsors,
    })


class Feedback(TemplateView):
    template_name= "feedback.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feed']=Testimonial.objects.all()
        context['header']=Header.objects.first()
        return context
    
class JobAdd(CreateView):
    template_name='job.html'    
    model=Jobs
    form_class =JobForm
    success_url=reverse_lazy('h')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data']=Jobs.objects.all()
        return context
    def form_valid(self, form):
        if form.is_valid():
            return super().form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)