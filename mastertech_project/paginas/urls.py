from django.urls import path
from .views import HomePageView
from .views import BookListView,BookDetails,SearchResultsListView,NovoLivro,EditarLivro,DeletarLivro

urlpatterns = [ 
        path('',HomePageView.as_view(),name='home'),
        path('livros/',BookListView.as_view(),name='book_list'),
        path('livros/<uuid:pk>',BookDetails.as_view(),name='book_details'),
        path('livros/pesquisa',SearchResultsListView.as_view(),name='search_results'),
        path('livros/novo/',NovoLivro.as_view(),name='novo_livro'),
        path('livros/<uuid:pk>/edit/', EditarLivro.as_view(),name='editar_livro'),
        path('livros/<uuid:pk>/delete/',DeletarLivro.as_view(),name='deletar_livro'),
    
]
