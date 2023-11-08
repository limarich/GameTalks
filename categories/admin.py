from django import forms
from django.contrib import admin

from .models import Category, Forum

class ForumAdminForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        to_field_name='title'
    )

class ForumAdmin(admin.ModelAdmin):
    form = ForumAdminForm

admin.site.register(Category)
admin.site.register(Forum, ForumAdmin)
