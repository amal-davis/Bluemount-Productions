from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index(request):
    videos = Video.objects.all()
    images = GalleryImage.objects.all().order_by('-id')
    positions = CareerPosition.objects.all().order_by('-id')

    return render(request,'index.html',{'videos':videos,'images':images,'positions':positions})



def add_video(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        youtube_url = request.POST.get('youtube_url')
        if title and youtube_url:
            Video.objects.create(title=title, youtube_url=youtube_url)
            return redirect('add_video')  # Redirect to the portfolio page or any other page
        else:
            return HttpResponse("Title and URL are required.", status=400)
    videos = Video.objects.all()
    return render(request, 'add_video.html',{'videos':videos})


def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.delete()
    return redirect('add_video')




def edit_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video.title = request.POST.get('title')
        video.youtube_url = request.POST.get('youtube_url')
        video.save()
        return redirect('add_video')
    return render(request, 'edit_video.html', {'video': video})



def gallery_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        if title and image:
            GalleryImage.objects.create(title=title, image=image)
            return redirect('gallery_view')
        else:
            return HttpResponse("Title and image are required.", status=400)
    
    images = GalleryImage.objects.all()
    return render(request, 'add_gallery.html', {'images': images})



def delete_image(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    image.delete()
    return redirect('gallery_view')



def career_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            CareerPosition.objects.create(title=title, description=description)
            return redirect('career_view')
        else:
            return HttpResponse("Title and description are required.", status=400)
    
    positions = CareerPosition.objects.all().order_by('-id')  # Order by id in descending order
    return render(request, 'add_career.html', {'positions': positions})


def delete_position(request, position_id):
    position = get_object_or_404(CareerPosition, id=position_id)
    position.delete()
    return redirect('career_view')


def edit_position(request, position_id):
    position = get_object_or_404(CareerPosition, id=position_id)
    if request.method == 'POST':
        position.title = request.POST.get('title')
        position.description = request.POST.get('description')
        position.save()
        return redirect('career_view')
    return render(request, 'edit_position.html', {'position': position})


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if name and email and message:
            # Save the contact form data in the database
            Contact.objects.create(name=name, email=email, phone=phone, message=message)
            
            # Send an email to the admin
            admin_email = 'amald416@gmail.com'  # Replace with admin's email
            subject = f"New Contact Form Submission from {name}"
            message_body = f"""
            Name: {name}
            Email: {email}
            Phone: {phone}
            Message: {message}
            """
            send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [admin_email])
            
            return redirect('/#contact-form')  # Redirect to the form section
        else:
            return HttpResponse("Name, Email, and Message are required.", status=400)
    
    return render(request, 'index.html')


def contact_list_view(request):
    contacts = Contact.objects.all().order_by('-id') # Retrieve all contacts and order by latest
    return render(request, 'contact_list.html', {'contacts': contacts})


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('contact_list')


def admin_page(request):
    return render(request,'admin.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_page')  # Redirect to the contact list or any other page after login
        else:
            return HttpResponse("Invalid username or password", status=400)
    return render(request, 'login.html')