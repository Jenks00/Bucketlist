from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import To_do


class CustomLoginView(LoginView):
    template_name = 'bucket_list/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task')


class RegisterPage(FormView):
    template_name = 'bucket_list/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)



class To_doList(LoginRequiredMixin, ListView):
    model = To_do
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                Task__contains=search_input)

        context['search_input'] = search_input

        return context



class To_doCreate(LoginRequiredMixin, CreateView):
    model = To_do
    fields = ['Task', 'Time_required', 'complete']
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.complete:
            form.instance.completed = timezone.now()
        return super(To_doCreate, self).form_valid(form)


class To_doUpdate(LoginRequiredMixin, UpdateView):
    model = To_do
    fields = ['Task', 'Time_required', 'complete']
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        if form.instance.complete and not form.instance.completed:
            form.instance.completed = timezone.now()
        elif not form.instance.complete:
            form.instance.completed = None
        return super(To_doUpdate, self).form_valid(form)


class To_doDelete(LoginRequiredMixin, DeleteView):
    model = To_do
    context_object_name = 'task'
    success_url = reverse_lazy('task')


    




