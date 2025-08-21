from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .models import Skill, Project

def home(request):
    return render(request, "home.html")

def about(request):
    skills = [
        {"name": "Python", "level": "Expert"},
        {"name": "Django", "level": "Advanced"},
        {"name": "React", "level": "Intermediate"},
        {"name": "MySQL", "level": "Intermediate"},
    ]
    return render(request, "about.html", {"skills": skills})


def projects(request):
    project_list = [
        {
            "title": "Baby Products",
            "description": "Built with Django + MySQL",
            "link": "https://baby-products-chi.vercel.app/",
            
        },
        {
            "title": "Cherii Bakery",
            "description": "Build with React & Tailwind",
            "link": "https://cherri-bakery.vercel.app/",
            
        },
    ]
    return render(request, "projects.html", {"projects": project_list})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # Send email
            send_mail(
                subject=f"Portfolio Contact Form - {name}",
                message=f"Message from {name} ({email}):\n\n{message}",
                from_email=email,
                recipient_list=["rockyranjith1121@gmail.com"], 
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
