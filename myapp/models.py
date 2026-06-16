from django.db import models

from django.db import models

class Hero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500)
    background_image = models.ImageField(upload_to='hero_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    from django.db import models

from django.db import models

class AboutSection(models.Model):
    # Main info
    heading = models.CharField(max_length=200)
    subtitle = models.TextField()
    description = models.TextField(blank=True)

    # Personal info fields
    birthday = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=100, blank=True)
    age = models.CharField(max_length=10, blank=True)
    degree = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)
    freelance = models.CharField(max_length=50, blank=True)
    
    # Profile image
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    # Skills
    skill_html = models.IntegerField(default=0)
    skill_css = models.IntegerField(default=0)
    skill_js = models.IntegerField(default=0)
    skill_php = models.IntegerField(default=0)
    skill_wordpress = models.IntegerField(default=0)
    skill_photoshop = models.IntegerField(default=0)
    
    # Resume fields (summary, education, experience as text fields)
    summary = models.TextField(blank=True)
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading
    from django.db import models

# Portfolio Items (Client Winning System)
class PortfolioItem(models.Model):

    CATEGORY_CHOICES = [
        ('app', 'App'),
        ('product', 'Product'),
        ('branding', 'Web'),
    ]

    title = models.CharField(max_length=200)

    # Optional but powerful for trust
    client_name = models.CharField(max_length=200, blank=True, null=True)

    # Case study structure (THIS IS WHAT CLIENTS CARE ABOUT)
    problem = models.TextField(blank=True, null=True)
    solution = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)

    # fallback short description
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='portfolio/')

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='app'
    )

    # optional live link (VERY IMPORTANT FOR CLIENT TRUST)
    project_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Testimonials
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Optional: Portfolio section intro
class PortfolioIntro(models.Model):
    subtitle = models.CharField(max_length=300, default="Welcome to my Portfolio section.")

    def __str__(self):
        return "Portfolio Intro"

# Optional: Testimonials section intro
class TestimonialIntro(models.Model):
    subtitle = models.CharField(max_length=300, default="What my clients say about me.")

    def __str__(self):
        return "Testimonials Intro"
    from django.db import models

class Service(models.Model):
    icon = models.CharField(max_length=100, default="bi bi-activity")  # Bootstrap icon class
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    from django.db import models

class ContactInfo(models.Model):
    address = models.CharField(max_length=255, default="A108 Adam Street, New York, NY 535022")
    phone = models.CharField(max_length=50, default="+1 5589 55488 55")
    email = models.EmailField(default="info@example.com")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Contact Info"
    from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField(default=0)  # for progress bar %

    def __str__(self):
        return self.name
    from django.db import models

class ResumeEntry(models.Model):
    title = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=200, blank=True)
    start_year = models.CharField(max_length=10, blank=True)
    end_year = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=50, choices=[('education', 'Education'), ('experience', 'Experience')])

    def __str__(self):
        return f"{self.type}: {self.title or self.degree}"