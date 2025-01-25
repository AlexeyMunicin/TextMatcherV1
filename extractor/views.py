from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from .utils import TextMatcher

def image_upload(request):
    text = None
    image_url = None

    if request.method == 'POST' and request.FILES['image']:
        # Сохранение файла изображения
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_image_url = fs.url(filename)

        # Извлечение текста с изображения
        matcher = TextMatcher()
        text = matcher.extract_text(f'.{uploaded_image_url}')

        image_url = uploaded_image_url

    return render(request, 'extractor/upload.html', {'text': text, 'image_url': image_url})
