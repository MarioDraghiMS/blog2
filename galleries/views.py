from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Gallery, Photo
from .forms import GalleryForm, PhotoForm

def gallery_list(request):
    galleries = Gallery.objects.all()
    return render(request, 'galleries/gallery_list.html', {'galleries': galleries})

@login_required
def gallery_create(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.author = request.user
            gallery.save()
            return redirect('gallery_list')
    else:
        form = GalleryForm()
    return render(request, 'galleries/gallery_form.html', {'form': form})

def gallery_detail(request, gallery_id):
    gallery = get_object_or_404(Gallery, id=gallery_id)
    return render(request, 'galleries/gallery_detail.html', {'gallery': gallery})

@login_required
def photo_add(request, gallery_id):
    gallery = get_object_or_404(Gallery, id=gallery_id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.gallery = gallery
            photo.save()
            return redirect('gallery_detail', gallery_id=gallery.id)
    else:
        form = PhotoForm()
    return render(request, 'galleries/photo_form.html', {'form': form, 'gallery': gallery})
