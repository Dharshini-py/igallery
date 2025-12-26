from django.shortcuts import render
def gallery_view(request):
    images = [
        'image1.jpg',
        'image2.jpg',
        'image3.jpg',
        'image4.jpg',
        'image5.jpg',
    ]
    return render(request, 'myapp/gallery.html', {'images': images})