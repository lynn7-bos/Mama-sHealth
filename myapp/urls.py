
from django.contrib import admin
from django.urls import path
from myapp import views

import myapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('explore/', views.explore, name='explore'),
    path('myservice/', views.myservice, name='myservice'),
    path('appointment/', views.appointment, name='appointment'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('support/', views.support, name='support'),
    path('donation/', views.donation, name='donation'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
    path('community/', views.community, name='community'),
    path('faq/', views.faq, name='faq'),
    path('article_1/', views.article_1, name='article_1'),
    path('bptracker/', views.bp_tracker, name='bptracker'),
    path('watertracker/', views.watertracker, name='watertracker'),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),

]
