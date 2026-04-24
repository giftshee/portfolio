from django import forms
from .models import Skill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'percent']  # adjust based on your model
        from django import forms
from .models import ResumeEntry

class ResumeEntryForm(forms.ModelForm):
    class Meta:
        model = ResumeEntry
        fields = '__all__'
        from django import forms
from django import forms
from .models import AboutSection

class AboutSectionForm(forms.ModelForm):
    class Meta:
        model = AboutSection
        fields = [
            'heading', 'subtitle', 'description', 'birthday', 'website', 'phone',
            'city', 'age', 'degree', 'email', 'freelance', 'image'  # ✅ include 'image'
        ]
        from django import forms
from .models import Hero

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['title', 'subtitle', 'background_image']