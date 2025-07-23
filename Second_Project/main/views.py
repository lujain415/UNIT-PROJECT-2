from django.shortcuts import render, redirect
from pets.models import Pet
from .forms import ContactForm
from .models import Contact

def home(request):
    
    featured_pets = Pet.objects.filter(available=True).order_by('-created_at')[:6]
    return render(request, 'main/home.html', {'pets': featured_pets})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('main:contact_success')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def contact_messages_view(request):
    messages = Contact.objects.all().order_by('-created_at')
    return render(request, 'main/contact_messages.html', {'messages': messages})

def contact_success_view(request):
    return render(request, 'main/contact_success.html')


def pet_list(request):
    
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

def pet_detail(request, pet_id):
    from django.shortcuts import get_object_or_404
    pet = get_object_or_404(Pet, id=pet_id)
    comments = pet.comments.order_by('-created_at')

    if request.method == 'POST':
        from .forms import CommentForm
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pet = pet
            comment.save()
            return redirect('main:detail', pet_id=pet.id)
    else:
        from .forms import CommentForm
        form = CommentForm()

    return render(request, 'main/detail.html', {
        'pet': pet,
        'comments': comments,
        'form': form,
    })
