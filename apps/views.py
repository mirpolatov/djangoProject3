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

    # Construct the full URL
    full_url = request.build_absolute_uri(document.pdf_file.url)

    # Create QR code
    qr = qrcode.make(full_url)

    # Create an HTTP response with the QR code image
    response = HttpResponse(content_type='image/png')
    qr.save(response, 'PNG')

    # Set the Content-Disposition header to prompt download
    response['Content-Disposition'] = 'attachment; filename="qr_code.png"'

    return response

