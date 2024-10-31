import qrcode
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Document

def generate_qr_code(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    url = request.build_absolute_uri(document.pdf_file.url)

    # QR kod yaratish
    qr = qrcode.make(url)
    response = HttpResponse(content_type="image/png")
    qr.save(response, "PNG")
    return response
