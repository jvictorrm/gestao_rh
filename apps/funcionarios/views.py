from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionariosNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.empresa = self.request.user.funcionario.empresa
        obj.user = User.objects.create(username=''.join(obj.nome.split(' ')))
        obj.save()
        return super(FuncionariosNovo, self).form_valid(form)


class FuncionariosEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionariosDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')
