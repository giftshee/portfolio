# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test

from .models import (
    Hero, AboutSection, Skill, ResumeEntry, Service,
    PortfolioItem, Testimonial, PortfolioIntro, TestimonialIntro,
    ContactInfo
)
from .forms import SkillForm, ResumeEntryForm

# Admin check decorator
admin_required = user_passes_test(lambda u: u.is_superuser)

# ---------------- Home / Hero ----------------
def home(request):
    hero = Hero.objects.first()
    return render(request, 'myapp/index.html', {'hero': hero})

from django.shortcuts import get_object_or_404, redirect
from .models import Hero
# from .decorators import admin_required  # Assuming you have this

@admin_required
def hero_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        bg_image = request.FILES.get('background_image')  # get uploaded file
        if title and subtitle:
            hero = Hero.objects.create(title=title, subtitle=subtitle)
            if bg_image:
                hero.background_image = bg_image
                hero.save()
    return redirect('home')


@admin_required
def hero_edit(request, pk):
    hero = get_object_or_404(Hero, pk=pk)
    if request.method == 'POST':
        hero.title = request.POST.get('title', hero.title)
        hero.subtitle = request.POST.get('subtitle', hero.subtitle)
        bg_image = request.FILES.get('background_image')
        if bg_image:
            hero.background_image = bg_image
        hero.save()
    return redirect('home')

@admin_required
def hero_delete(request, pk):
    hero = get_object_or_404(Hero, pk=pk)
    if request.method == 'POST':
        hero.delete()
    return redirect('home')


from django.shortcuts import render, get_object_or_404, redirect
from .models import AboutSection
from django.contrib.auth.decorators import user_passes_test

# Superuser-only decorator
admin_required = user_passes_test(lambda u: u.is_superuser)

# About page
def about(request):
    about_section = AboutSection.objects.first()
    skills = Skill.objects.all()
    resume_entries = ResumeEntry.objects.all()
    context = {
        'about': about_section,
        'skills': skills,
        'resume_entries': resume_entries,
    }
    return render(request, 'myapp/about.html', context)

# Add About section
from django.shortcuts import render, get_object_or_404, redirect
from .models import AboutSection
from .forms import AboutSectionForm

# Add About
@admin_required
def about_add(request):
    if request.method == 'POST':
        form = AboutSectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = AboutSectionForm()
    return render(request, 'myapp/about_form.html', {'form': form, 'title': 'Add About'})

# Edit About
@admin_required
def about_edit(request, pk):
    about = get_object_or_404(AboutSection, pk=pk)
    if request.method == 'POST':
        form = AboutSectionForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = AboutSectionForm(instance=about)
    return render(request, 'myapp/about_form.html', {'form': form, 'title': 'Edit About'})

# Delete About section
@admin_required
def about_delete(request, pk):
    about = get_object_or_404(AboutSection, pk=pk)
    if request.method == 'POST':
        about.delete()
    return redirect('about')


# ---------------- Skills ----------------
@admin_required
def skill_add(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = SkillForm()
    return render(request, 'myapp/skill_form.html', {'form': form})

@admin_required
def skill_edit(request, id):
    skill = get_object_or_404(Skill, id=id)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'myapp/skill_form.html', {'form': form})

@admin_required
def skill_delete(request, id):
    skill = get_object_or_404(Skill, id=id)
    if request.method == 'POST':
        skill.delete()
        return redirect('about')
    return render(request, 'myapp/skill_confirm_delete.html', {'skill': skill})


# ---------------- Resume ----------------
@admin_required
def resume_add(request):
    if request.method == "POST":
        form = ResumeEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = ResumeEntryForm()
    return render(request, 'myapp/resume_form.html', {'form': form})

@admin_required
def resume_edit(request, pk):
    entry = get_object_or_404(ResumeEntry, pk=pk)
    if request.method == "POST":
        form = ResumeEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = ResumeEntryForm(instance=entry)
    return render(request, 'myapp/resume_form.html', {'form': form})

@admin_required
def resume_delete(request, pk):
    entry = get_object_or_404(ResumeEntry, pk=pk)
    if request.method == "POST":
        entry.delete()
        return redirect('about')
    return render(request, 'myapp/resume_confirm_delete.html', {'entry': entry})


# ---------------- Services ----------------
def services_page(request):
    services = Service.objects.all()
    return render(request, 'myapp/services.html', {'services': services})

@admin_required
def service_add(request):
    if request.method == "POST":
        Service.objects.create(
            icon=request.POST.get('icon', 'bi bi-activity'),
            title=request.POST['title'],
            description=request.POST['description']
        )
    return redirect('services')

@admin_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        service.icon = request.POST.get('icon', service.icon)
        service.title = request.POST['title']
        service.description = request.POST['description']
        service.save()
    return redirect('services')

@admin_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    return redirect('services')


# ---------------- Portfolio & Testimonials ----------------
def portfolio_page(request):
    portfolio_items = PortfolioItem.objects.all()
    testimonials = Testimonial.objects.all()
    portfolio_intro = PortfolioIntro.objects.first()
    testimonials_intro = TestimonialIntro.objects.first()
    return render(request, 'myapp/portfolio.html', {
        'portfolio_items': portfolio_items,
        'testimonials': testimonials,
        'portfolio_intro': portfolio_intro,
        'testimonials_intro': testimonials_intro
    })

def portfolio_detail(request, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    return render(request, 'myapp/portfolio_detail.html', {'item': item})

@admin_required
def portfolio_add(request):
    if request.method == "POST":
        PortfolioItem.objects.create(
            title=request.POST['title'],
            description=request.POST.get('description',''),
            category=request.POST['category'],
            image=request.FILES['image']
        )
    return redirect('portfolio')

@admin_required
def portfolio_edit(request, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    if request.method == "POST":
        item.title = request.POST['title']
        item.description = request.POST.get('description','')
        item.category = request.POST['category']
        if 'image' in request.FILES:
            item.image = request.FILES['image']
        item.save()
    return redirect('portfolio')

@admin_required
def portfolio_delete(request, pk):
    item = get_object_or_404(PortfolioItem, pk=pk)
    item.delete()
    return redirect('portfolio')

@admin_required
def testimonial_add(request):
    if request.method == "POST":
        Testimonial.objects.create(
            name=request.POST['name'],
            title=request.POST['title'],
            text=request.POST['text'],
            image=request.FILES['image']
        )
    return redirect('portfolio')

@admin_required
def testimonial_edit(request, pk):
    t = get_object_or_404(Testimonial, pk=pk)
    if request.method == "POST":
        t.name = request.POST['name']
        t.title = request.POST['title']
        t.text = request.POST['text']
        if 'image' in request.FILES:
            t.image = request.FILES['image']
        t.save()
    return redirect('portfolio')

@admin_required
def testimonial_delete(request, pk):
    t = get_object_or_404(Testimonial, pk=pk)
    t.delete()
    return redirect('portfolio')


# ---------------- Contact ----------------
def contact_page(request):
    contact = ContactInfo.objects.first()
    return render(request, 'myapp/contact.html', {'contact': contact})

@admin_required
def contact_edit(request):
    contact = ContactInfo.objects.first()
    if request.method == "POST":
        if contact:
            contact.address = request.POST['address']
            contact.phone = request.POST['phone']
            contact.email = request.POST['email']
            contact.save()
        else:
            ContactInfo.objects.create(
                address=request.POST['address'],
                phone=request.POST['phone'],
                email=request.POST['email']
            )
    return redirect('contact')
def team(request):
    resume_entries = ResumeEntry.objects.all()
    skills = Skill.objects.all()
    about = AboutSection.objects.first()
    return render(request, 'myapp/about.html', {
        'about': about,
        'skills': skills,
        'resume_entries': resume_entries
    })