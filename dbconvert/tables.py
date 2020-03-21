import django_tables2 as tables
from django_tables2 import A

from .models import Cruzada

class TabelaCruzada(tables.Table):

    class Meta:
        model = Cruzada
        template_name = "django_tables2/bootstrap4.html"
        fields = ('Cod_mercadoria', 'Desc_mercadoria', 'Prioridade', 'Voltagem_item', 'Voltagem_filial', 'Vigencia_inicio', 'Vigencia_fim', 'Cod_Tamanho', 'Desc_Tamanho')

        orderable = True

