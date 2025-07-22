from django.contrib import admin

# Register your models here.

from .models import Pet, Comment
# Register your models here.



@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed', 'category', 'available', 'created_at')
    list_filter = ('category', 'available')
    search_fields = ('name', 'breed', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'pet', 'created_at')
    search_fields = ('name', 'text')
