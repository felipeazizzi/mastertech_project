from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Livros
from django_tables2 import SingleTableView
from .tables import LivrosTable
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'



class BookListView(SingleTableView):
    model= Livros
    template_name = 'book_list.html'
    table_class = LivrosTable

    def get_queryset(self):
        query=self.request.GET.get('q')
        return Livros.objects.all()

class BookDetails(DetailView):
    model=Livros
    template_name = 'book_details.html'

class SearchResultsListView(SingleTableView):
    model = Livros
    table_class = LivrosTable
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Livros.objects.filter(
                Q(titulo__icontains=query) | Q(autor__icontains=query)
        )

class NovoLivro(LoginRequiredMixin,CreateView):
    model= Livros
    template_name= 'novo_livro.html'
    fields ='__all__'

class EditarLivro(LoginRequiredMixin,UpdateView):
    model=Livros
    template_name='editar_livro.html'
    fields='__all__'

class DeletarLivro(LoginRequiredMixin,DeleteView):
    model=Livros
    template_name='deletar_livro.html'
    success_url = reverse_lazy('home')
