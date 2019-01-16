from django.urls import path
from .views import RegistroHoraExtraList, RegistroHoraExtraNovo, RegistroHoraExtraEdit, RegistroHoraExtraDelete

urlpatterns = [
    path('', RegistroHoraExtraList.as_view(), name='list_hora_extra'),
    path('novo', RegistroHoraExtraNovo.as_view(), name='create_hora_extra'),
    path('editar/<int:pk>', RegistroHoraExtraEdit.as_view(), name='edit_hora_extra'),
    path('deletar/<int:pk>', RegistroHoraExtraDelete.as_view(), name='delete_hora_extra')
]
