from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from apps.documentos.models import Documento


class DepartamentosList(ListView):
    model = Documento

    def get_queryset(self):
        funcionario = self.request.user.funcionario
        return Documento.objects.filter(funcionario=funcionario)


class DocumentosNovo(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']

        if form.is_valid(self):
            return self.form_valid(form)

        return self.form_invalid(form)


class DocumentosDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy('list_funcionarios')

