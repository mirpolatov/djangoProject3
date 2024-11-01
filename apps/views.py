import os
from audioop import reverse

import qrcode
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Document


def document_list(request):
    documents = Document.objects.all()
    return render(request, 'documents.html', {'documents': documents})


def upload_document(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']
        title = request.POST.get('title')
        pin = request.POST.get('pin')
        document = Document(title=title, pdf_file=pdf_file, pin=pin)
        document.save()
        return redirect('document_list')
    return render(request, 'upload.html')


# def verify_pin(request, document_id):
#     document = get_object_or_404(Document, id=document_id)
#
#     if request.method == 'POST':
#         entered_pin = request.POST.get('pin')
#         if entered_pin == document.pin:
#             return redirect(document.pdf_file.url)
#         else:
#             return render(request, 'verify_pin.html', {'error': 'не правильно ПИН код.', 'document_id': document_id})
#
#     return render(request, 'verify_pin.html', {'document_id': document_id})


def verify_pin(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    if request.method == 'POST':
        entered_pin = request.POST.get('pin')

        if entered_pin == document.pin:
            # Serve the PDF file
            response = HttpResponse(document.pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="{document.pdf_file.name}"'
            return response
        else:
            # Incorrect PIN; return an error message
            return render(request, 'verify_pin.html', {'error': 'не правильно ПИН код.'})

    return render(request, 'verify_pin.html')


# def generate_qr_code(request, document_id):
#     document = Document.objects.get(id=document_id)
#
#
#     full_url = request.build_absolute_uri(document.pdf_file.url)
#
#
#     qr = qrcode.make(full_url)
#
#
#     response = HttpResponse(content_type='image/png')
#     qr.save(response, 'PNG')
#
#
#     response['Content-Disposition'] = 'attachment; filename="qr_code.png"'
#
#     return response

def generate_qr_code(request, document_id):
    verification_url = request.build_absolute_uri(f'/verify-pin/{document_id}/')

    qr = qrcode.make(verification_url)

    response = HttpResponse(content_type='image/png')
    qr.save(response, 'PNG')

    return response


def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        document.delete()
        return redirect(('document_list'))
