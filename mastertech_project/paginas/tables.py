import django_tables2 as tables
from django_tables2.utils import A
from .models import Livros

class LivrosTable(tables.Table):
    titulo = tables.LinkColumn("book_details",args=[A("pk")])
    dispon = tables.Column(verbose_name='Disponibilidade')
    class Meta:
        model = Livros
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ("titulo","autor","dispon")

