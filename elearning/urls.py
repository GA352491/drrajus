from django.contrib import admin
from django.urls import path
from elearning import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('consultancy/', views.consultancy, name='consultancy'),
    path('contact/', views.contact, name='contact'),
    path('forum/', views.forum, name='forum'),
    path('about_us/', views.about_us, name='About Us'),
    # path('payment/', views.gre_payment, name='payment'),
    # path('payment2/', views.secondary_payment, name='payment2'),
    # path('payment3/', views.special_payment, name='payment3'),
    # path('success/', views.success, name='success'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('blog/', views.blog, name='blog'),
    path('blog_view/<pk>', views.blog_view, name='blog_view'),
    path('content/', views.content, name='content'),
    path('email/', views.email, name='email'),
]
