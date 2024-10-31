from django.urls import path
from .views import document_list, upload_document, generate_qr_code, upload_pdf

urlpatterns = [
    path('', document_list, name='document_list'),
    path('upload/', upload_document, name='upload_document'),
    path('document/<int:document_id>/qr/', generate_qr_code, name='generate_qr_code'),
    path('upload_pdf/', upload_pdf, name='upload_pdf'),
]
