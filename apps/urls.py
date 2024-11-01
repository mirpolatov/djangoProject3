from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('documents/', views.document_list, name='document_list'),
    path('upload/', views.upload_document, name='upload_document'),
    path('generate-qr/<int:document_id>/', views.generate_qr_code, name='generate_qr_code'),
    path('verify-pin/<int:document_id>/', views.verify_pin, name='verify_pin'),
    path('document/<int:document_id>/delete/', views.delete_document, name='delete_document'),
]


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404_view