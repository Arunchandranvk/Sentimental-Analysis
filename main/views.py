from django.shortcuts import render, redirect
from .models import Header, Home, Callback, Title, Service, Info, Count, About, Testimonial, Contact, Sponsor, FooterContact
from .forms import ContactModelForm, FooterContactModelForm ,FeedbackModelForm

# Create your views here.

def index(request):
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
        form3 = FeedbackModelForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('/')
        if form2.is_valid():
            FooterContact.objects.create(**form2.cleaned_data)
            return redirect('/')
        if form3.is_valid():
            Testimonial.objects.create(**form3.cleaned_data)
            return redirect('/')
    else:
        form = ContactModelForm()

    return render(request, 'index.html', context={
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