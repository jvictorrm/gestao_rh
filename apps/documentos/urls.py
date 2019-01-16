from django.urls import path
from .views import DocumentosNovo, DocumentosDelete # , DepartamentosEdit, DocumentosList

urlpatterns = [
    # path('', DocumentosList.as_view(), name='list_documentos'),
    path('novo/<int:funcionario_id>/', DocumentosNovo.as_view(), name='create_documento'),
    # path('editar/<int:pk>', DepartamentosEdit.as_view(), name='edit_departamento'),
    path('deletar/<int:pk>', DocumentosDelete.as_view(), name='delete_documento'),
]
