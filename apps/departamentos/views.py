from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Departamento


class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentosNovo(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.empresa = self.request.user.funcionario.empresa
        obj.save()
        return super(DepartamentosNovo, self).form_valid(form)


class DepartamentosEdit(UpdateView):
    model = Departamento
    fields = ['nome']


class DepartamentosDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')
