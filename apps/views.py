from django.shortcuts import render, redirect
from .models import Document
from django.core.files.storage import FileSystemStorage
import qrcode
from django.http import HttpResponse
import os


def document_list(request):
    documents = Document.objects.all()
    return render(request, 'documents.html', {'documents': documents})


def upload_document(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']
        title = request.POST.get('title')
        document = Document(title=title, pdf_file=pdf_file)
        document.save()
        return redirect('document_list')
    return render(request, 'upload.html')


def generate_qr_code(request, document_id):
    document = Document.objects.get(id=document_id)
    qr = qrcode.make(document.pdf_file.url)

    # QR kodini vaqtinchalik fayl sifatida saqlash
    response = HttpResponse(content_type='image/png')
    qr.save(response, 'PNG')
    return response
