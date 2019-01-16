from django.urls import path
from .views import DepartamentosList, DepartamentosNovo, DepartamentosEdit, DepartamentosDelete

urlpatterns = [
    path('', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo', DepartamentosNovo.as_view(), name='create_departamento'),
    path('editar/<int:pk>', DepartamentosEdit.as_view(), name='edit_departamento'),
    path('deletar/<int:pk>', DepartamentosDelete.as_view(), name='delete_departamento'),
]
