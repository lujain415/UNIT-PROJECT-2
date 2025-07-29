from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse

from pets.models import Pet
from .models import Contact

from .forms import ContactForm
from pets.forms import CommentForm

def home(request: HttpRequest):
    return render(request, 'main/home.html')


def contact_view(request: HttpRequest):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            new_contact = Contact(name=name, email=email, message=message)
            new_contact.save()

            return redirect("main:contact_success")
    else:
        form = ContactForm()

    return render(request, "main/contact.html", {"form": form})


def contact_messages_view(request: HttpRequest):
    messages = Contact.objects.all().order_by('-created_at')
    return render(request, 'main/contact_messages.html', {'messages': messages})


def contact_success_view(request: HttpRequest):
    return render(request, 'main/contact_success.html')


def pet_list(request: HttpRequest):
    pets = Pet.objects.filter(available=True).order_by('-created_at')

    category = request.GET.get('category')
    if category and category != 'all':
        pets = pets.filter(category=category)

    context = {
        'pets': pets,
        'selected_category': category or 'all',
        'categories': Pet._meta.get_field('category').choices,
    }

    return render(request, 'main/pet_list.html', context)


def pet_detail(request: HttpRequest, pet_id: int):
    pet = get_object_or_404(Pet, id=pet_id)
    comments = pet.comments.order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pet = pet
            comment.save()
            return redirect('main:detail', pet_id=pet.id)
    else:
        form = CommentForm()

    return render(request, 'main/detail.html', {
        'pet': pet,
        'comments': comments,
        'form': form,
    })
