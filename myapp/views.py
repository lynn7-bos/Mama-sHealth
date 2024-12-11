import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth

from myapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from myapp.forms import AppointmentForm, ImageUploadForm
from myapp.models import Appointment, User, ImageModel


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

def about(request):
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

def community(request):
    return render(request,'community.html')

def watertracker(request):
    return render(request,'watertracker.html')

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
            answer = "There are regular strong contraction and Water(Amniotic fluid) breaks"
        elif "vaccination" in question.lower():
            answer = "BCG , Hepatitis B, and Oral Polio Vaccine"
        elif "stress" in question.lower():
            answer = "Yes,stress does affect pregnancy at some point"


        return render(request, 'faq.html', {'answer': answer})
    else:
        return render(request, 'faq.html')


def community(request):
    if request.method == 'POST':
        post_content = request.POST.get('post_content')
        request.session.setdefault('posts', []).append({'content': post_content, 'user': request.user.username})
    posts = request.session.get('posts', [])
    return render(request, 'community.html', {'posts': posts})

def bp_tracker(request):
    if request.method == 'POST':
        systolic = request.POST.get('systolic')
        diastolic = request.POST.get('diastolic')
        request.session.setdefault('bp_readings', []).append({'systolic': systolic, 'diastolic': diastolic})
    bp_readings = request.session.get('bp_readings', [])
    return render(request, 'BPtracker.html', {'bp_readings': bp_readings})

def token(request):
    consumer_key = 'DGwiuGpYAezZ7ZH7XCnlWy5H6eSDZzdAUgUOAG4iiEuZCnWl'
    consumer_secret = 'yuCJASr5jGaTyi9dTwBNkA5N1uUhSeRkIR77vp6xIeiupJZXOliWfNcvjhUgGYPu'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')





def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")


def watertracker(request):
    if request.method == 'POST':
        intake = float(request.POST.get('water'))
        request.session['water_intake'] = request.session.get('water_intake', 0) + intake
    water_intake = request.session.get('water_intake', 0)
    return render(request, 'watertracker.html', {'water_intake': water_intake})
