from datetime import datetime
from django.db import connection
import pandas as pd
from django.forms import model_to_dict
from django.http import HttpResponse, request, HttpResponseForbidden
from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from .filters import CruzadaFilter
from .process_csv_sort import *
from .models import *
from .tables import TabelaCruzada


query = '''Select
    dbconvert_sortemp.Cod_mercadoria,
    dbconvert_sortemp.Desc_mercadoria,
    dbconvert_sortemp.Prioridade,
    dbconvert_sortemp.Qtde,
    dbconvert_sortemp.Voltagem,
    dbconvert_sortemp.Vigencia_inicio,
    dbconvert_sortemp.Vigencia_fim,
    dbconvert_sortemp.Status
From
    dbconvert_sortim Left Join
    dbconvert_sortemp On dbconvert_sortim.Cod_Sortimento = dbconvert_sortemp.Cod_sortimento And
            dbconvert_sortim.Cod_Secao = dbconvert_sortemp.Cod_secao
Where
    dbconvert_sortim.Filial = '1000' And
    dbconvert_sortim.Cod_Secao = '16'
Group By
    dbconvert_sortim.Filial,
    dbconvert_sortim.Cod_Secao,
    dbconvert_sortemp.Cod_mercadoria,
    dbconvert_sortemp.Desc_mercadoria,
    dbconvert_sortemp.Prioridade,
    dbconvert_sortemp.Qtde,
    dbconvert_sortemp.Voltagem,
    dbconvert_sortemp.Vigencia_inicio,
    dbconvert_sortemp.Vigencia_fim,
    dbconvert_sortemp.Status,
    dbconvert_sortemp.Desc_tamanho,
    dbconvert_sortemp.Cod_tamanho'''


def home1(request):
    a = csv_pandas()
    # row = [
    #     ((d) for d in Sortim.objects.all().values_list('Cod_Secao', 'Desc_Secao').distinct())
    # ]
    #
    # for i in row:
    #     for j in i:
    #         print(j, 'opa')
    #
    # now = datetime.now()


    return render(request,'listas.html', {'now': a})

class home(SingleTableMixin, FilterView):
    table_class = TabelaCruzada
    model = Cruzada
    template_name = "lista.html"
    filterset_class = CruzadaFilter






