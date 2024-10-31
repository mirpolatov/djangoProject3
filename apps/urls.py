from django.urls import path
from . import views

urlpatterns = [
    path('documents/', views.document_list, name='document_list'),
    path('upload/', views.upload_document, name='upload_document'),
    path('generate-qr/<int:document_id>/', views.generate_qr_code, name='generate_qr_code'),
    path('verify-pin/<int:document_id>/', views.verify_pin, name='verify_pin'),
]

