from django.shortcuts import render, get_object_or_404, redirect
from .forms import AdoptionRequestForm
from .models import AdoptionRequest

from .forms import PetForm, CommentForm
from .models import Pet, Comment


def pet_list(request):
    pets = Pet.objects.all()

    
    category = request.GET.get('category')
    available = request.GET.get('available')

    if category and category != 'all':
        pets = pets.filter(category=category)

    if available == 'true':
        pets = pets.filter(available=True)
    elif available == 'false':
        pets = pets.filter(available=False)

    context = {
        'pets': pets,
        'selected_category': category or 'all',
        'selected_available': available or 'all',
        'categories': Pet._meta.get_field('category').choices,
    }
    return render(request, 'pets/pet_list.html', context)


def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    comments = pet.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pet = pet
            comment.save()
            return redirect('pets:pet_detail', pet_id=pet.id)
    else:
        form = CommentForm()

    return render(request, 'pets/pet_detail.html', {
        'pet': pet,
        'comments': comments,
        'form': form,
    })

def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pets:pet_list')
    else:
        form = PetForm()
    return render(request, 'pets/pet_form.html', {'form': form})

def pet_update(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pets:pet_detail', pet_id=pet.id)
    else:
        form = PetForm(instance=pet)
    return render(request, 'pets/pet_form.html', {'form': form, 'update': True})

def pet_delete(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        pet.delete()
        return redirect('pets:pet_list')
    return render(request, 'pets/pet_confirm_delete.html', {'pet': pet})

def pet_search(request):
    query = request.GET.get('search', '')
    pets = Pet.objects.filter(name__icontains=query) if query else Pet.objects.none()
    return render(request, 'pets/pet_search.html', {'results': pets, 'query': query})


def adoption_request_view(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        form = AdoptionRequestForm(request.POST)
        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.pet = pet
            adoption_request.save()
            return redirect('pets:thank_you')
    else:
        form = AdoptionRequestForm()
    return render(request, 'pets/adoption_request.html', {'form': form, 'pet': pet})


def thank_you_view(request):
    return render(request, 'pets/thank_you.html')

def adoption_requests_list(request):
    requests = AdoptionRequest.objects.select_related('pet').all()  
    return render(request, 'pets/adoption_requests_list.html', {'requests': requests})

def delete_adoption_request(request, request_id):
    adoption_request = get_object_or_404(AdoptionRequest, id=request_id)
    adoption_request.delete()
    return redirect('pets:adoption_requests_list')
