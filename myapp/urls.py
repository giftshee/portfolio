from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('hero/add/', views.hero_add, name='hero_add'),
    path('hero/<int:pk>/edit/', views.hero_edit, name='hero_edit'),
    path('hero/<int:pk>/delete/', views.hero_delete, name='hero_delete'),

    path('about/', views.about, name='about'),
    path('about/add/', views.about_add, name='about_add'),
    path('about/<int:pk>/edit/', views.about_edit, name='about_edit'),
    path('about/<int:pk>/delete/', views.about_delete, name='about_delete'),
    path('resume/add/', views.resume_add, name='resume_add'),
    path('resume/<int:pk>/edit/', views.resume_edit, name='resume_edit'),
    path('resume/<int:pk>/delete/', views.resume_delete, name='resume_delete'),
    path('skills/add/', views.skill_add, name='skill_add'),
    path('skills/edit/<int:id>/', views.skill_edit, name='skill_edit'),
    path('skills/delete/<int:id>/', views.skill_delete, name='skill_delete'),
    path('services/', views.services_page, name='services'),

    # Service CRUD
    path('service/add/', views.service_add, name='service_add'),
    path('service/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('service/<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('portfolio/', views.portfolio_page, name='portfolio'),
    path('portfolio/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),

    # Portfolio CRUD
    path('portfolio/add/', views.portfolio_add, name='portfolio_add'),
    path('portfolio/<int:pk>/edit/', views.portfolio_edit, name='portfolio_edit'),
    path('portfolio/<int:pk>/delete/', views.portfolio_delete, name='portfolio_delete'),

    # Testimonial CRUD
    path('testimonial/add/', views.testimonial_add, name='testimonial_add'),
    path('testimonial/<int:pk>/edit/', views.testimonial_edit, name='testimonial_edit'),
    path('testimonial/<int:pk>/delete/', views.testimonial_delete, name='testimonial_delete'),
    path('resume/', views.team, name='team'),
        path('contact/', views.contact_page, name='contact'),
    path('contact/edit/', views.contact_edit, name='contact_edit'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]