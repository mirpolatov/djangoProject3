from django.shortcuts import render, redirect, get_object_or_404
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
        pin = request.POST.get('pin')  # Get the PIN from the form
        document = Document(title=title, pdf_file=pdf_file, pin=pin)
        document.save()
        return redirect('document_list')
    return render(request, 'upload.html')


def verify_pin(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    if request.method == 'POST':
        entered_pin = request.POST.get('pin')
        if entered_pin == document.pin:
            return redirect(document.pdf_file.url)  # Redirect to the PDF if PIN is correct
        else:
            return render(request, 'verify_pin.html', {'error': 'не правильно ПИН код.', 'document_id': document_id})

    return render(request, 'verify_pin.html', {'document_id': document_id})


# def generate_qr_code(request, document_id):
#     document = Document.objects.get(id=document_id)
#
#     # Construct the full URL
#     full_url = request.build_absolute_uri(document.pdf_file.url)
#
#     # Create QR code
#     qr = qrcode.make(full_url)
#
#     # Create an HTTP response with the QR code image
#     response = HttpResponse(content_type='image/png')
#     qr.save(response, 'PNG')
#
#     # Set the Content-Disposition header to prompt download
#     response['Content-Disposition'] = 'attachment; filename="qr_code.png"'
#
#     return response

def generate_qr_code(request, document_id):
    # Use the URL for the PIN verification view
    verification_url = request.build_absolute_uri(f'/verify-pin/{document_id}/')

    # Create QR code with the verification URL
    qr = qrcode.make(verification_url)

    # Create an HTTP response with the QR code image
    response = HttpResponse(content_type='image/png')
    qr.save(response, 'PNG')

    return response
