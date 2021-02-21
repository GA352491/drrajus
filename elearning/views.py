from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
import razorpay
import datetime
from datetime import date
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage

from .forms import PostForm


# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def courses(request):
    return render(request, 'courses/courses.html')


def consultancy(request):
    return render(request, 'application_guidance/Application_Guidance.html')


def contact(request):
    return render(request, 'contact.html')


def forum(request):
    return render(request, 'forum.html')


def about_us(request):
    return render(request, 'about_us/About_us.html')


@login_required(login_url='login')
def gre_payment(request):
    course = Courses.objects.get(course_name='GRE')
    if request.method == 'POST':
        course1 = Courses.objects.get(course_name='GRE')
        course_name = course.course_name
        amount = (course.price) * 100
        client = razorpay.Client(auth=('rzp_test_1WNHBgka1Pseyl', '6QCOEaww9teQTeIqhjt2oK34'))
        plan_id = 'plan_Fx6NdoS8VGgvOD'

        cus_id = client.customer.create({'name': request.user.username, 'email': request.user.email})

        sub_id = client.subscription.create(
            {'plan_id': plan_id, 'customer_id': cus_id['id'], 'total_count': 1})

        pay = client.order.create(
            {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        print(pay)
        course = Payment(user_name=request.user.username, amount=course.price, payment_id=sub_id['id'],
                         course=course_name,
                         secondary_course='NA', email=request.user.email, date_of_payment=datetime.date.today())
        course.save()
        context = {'pay': pay, 'course_name': course_name, 'course': course1, 'sub_id': sub_id}
        return render(request, 'payment.html', context)
    context = {'course': course}
    return render(request, 'payment.html', context)


@login_required(login_url='login')
def secondary_payment(request):
    if request.method == 'POST':
        name = request.POST.get('secondary_course')
        print(name)
        course = Courses.objects.get(course_name=name)
        course_name = course.course_name
        course_price = course.price
        amount = (course.price) * 100
        client = razorpay.Client(auth=('rzp_test_1WNHBgka1Pseyl', '6QCOEaww9teQTeIqhjt2oK34'))
        pay = client.order.create(
            {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        course = Payment(user_name=request.user.username, amount=course.price, payment_id=pay['id'], course=course_name,
                         secondary_course='NA', email=request.user.email, date_of_payment=date.today())
        course.save()
        context = {'pay': pay, 'course_name': course_name, 'course_price': course_price}
        return render(request, 'payment2.html', context)

    return render(request, 'payment2.html', )


@login_required(login_url='login')
def special_payment(request):
    if request.method == 'POST':
        name = request.POST.get('secondary_course')
        course = Courses.objects.get(course_name=name)
        course_name = course.course_name
        course_price = 19999
        amount = (19999) * 100
        client = razorpay.Client(auth=('rzp_test_1WNHBgka1Pseyl', '6QCOEaww9teQTeIqhjt2oK34'))
        pay = client.order.create(
            {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

        course = Payment(user_name=request.user, amount=course.price, payment_id=pay['id'], course='GRE',
                         secondary_course=name, email=request.user.email, date_of_payment=datetime.date.today())
        course.save()
        context = {'pay': pay, 'course_name': course_name, 'course_price': course_price}
        return render(request, 'payment3.html', context)
    return render(request, 'payment3.html', )


@login_required(login_url='login')
def success(request):
    if request.method == 'POST':
        a = request.POST
        order_id = ''
        print(a)
        for key, value in a.items():
            if key == 'razorpay_subscription_id':
                order_id = value
                break
        user = Payment.objects.filter(payment_id=order_id).first()
        print(user)
        user.paid = True
        user.save()
        msg_plain = render_to_string('email.txt')
        msg_html = render_to_string('New email template 2020-11-03-2.html')

        send_mail('your payment has been done', msg_plain, settings.EMAIL_HOST_USER, [user.email],
                  html_message=msg_html)
        print(Payment.objects.filter(paid=False))
        Payment.objects.filter(paid=False).delete()

    return render(request, 'success.html')


def terms(request):
    return render(request, 'terms and condition.html')


def privacy(request):
    return render(request, 'privacy policy.html')


def blog(request):
    form = PostForm()
    blogs = Blog.objects.order_by('id')
    paginator = Paginator(blogs, per_page=4)
    page_request_var = 'page'
    page = request.GET.get('page', 1)

    try:
        paginated_query_set = paginator.page(page)
    except PageNotAnInteger:
        paginated_query_set = paginator.page(1)
    except EmptyPage:
        paginated_query_set = paginator.page(paginator.num_pages)

    context = {'queryset': paginated_query_set, 'page_request_var': page_request_var, 'blogs': blogs, 'form': form}
    return render(request, 'blogs/blog.html', context)


def blog_view(request, pk):
    post = Blog.objects.get(id=pk)
    form = PostForm()
    context = {'post': post, 'form': form}
    return render(request, 'blogs/blog_view.html', context)


def content(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            print(a.content)

    return redirect('blog')
