from django.shortcuts import render, redirect
from myapp.models import Appointment, User, ImageModel, Member
from myapp.forms import AppointmentForm, ImageUploadForm


# reate your views here.

def index(request):
    if request.method=='POST':
        if User.objects.filter(
                username=request.POST['username'],
                password=request.POST['password'] ).exists():

             return render(request,'index.html')
        else:
             return render(request,'login.html')
    else:
        return render(request,'index.html')




def service(request):
    return render(request,'service-details.html')

def starter(request):
    return render(request,'starter-page.html')

def learn(request):
    return render(request,'learn.html')

def explore(request):
    return render(request,'explore.html')

def myservice(request):
    return render(request,'services.html')

def support(request):
    return render(request,'support.html')

def donation(request):
    return render(request,'donation.html')

def testimonial(request):
    return render(request,'testimonials.html')

def faq(request):
    return render(request,'faq.html')

def contact(request):
    return render(request,'contact.html')

def article_1(request):
    return render(request,'article-1.html')

def appointment(request):
    if request.method == "POST":
        myappointments=Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],

        )
        myappointments.save()
        return redirect('/appointment')


    else:
        return render(request,'appointment.html')


def show(request):
    allappointments=Appointment.objects.all()
    return render(request,'show.html',{'appointment':allappointments})

def delete(request,id):
    appoint = Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('/show')

def edit(request,id):
    editappointment=Appointment.objects.get(id=id)
    return render(request,'edit.html',{'appointment':editappointment})

def update(request,id):
    updateinfo = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST,instance = updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request,'edit.html')


def register(request):
    if request.method=='POST':
        members = User(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/login')

    else:
        return render(request, 'register.html')

def login(request):
    return render(request,'login.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def faq(request):
    question = request.GET.get('query')
    answer = None
    if question:
        # Simulated answers
        if "nutrition" in question.lower():
            answer = "A balanced diet rich in vegetables, fruits, and protein is vital during pregnancy."
        elif "exercise" in question.lower():
            answer = "Light exercise like walking or prenatal yoga is beneficial."
        elif "water" in question.lower():
            answer = "Take water 8 times a day."
        elif "labor" in question.lower():
            answer = "Regular strong contraction and Water(Amniotic fluid) breaks"
        elif "vaccination" in question.lower():
            answer = "BCG , Hepatitis B, and Oral Polio Vaccine"


        return render(request, 'faq.html', {'answer': answer})
    else:
        return render(request, 'faq.html')

