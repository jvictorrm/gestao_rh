from django.urls import path
from .views import FuncionariosList, FuncionariosNovo, FuncionariosEdit, FuncionariosDelete

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo', FuncionariosNovo.as_view(), name='create_funcionario'),
    path('editar/<int:pk>', FuncionariosEdit.as_view(), name='edit_funcionario'),
    path('deletar/<int:pk>', FuncionariosDelete.as_view(), name='delete_funcionario'),
]
