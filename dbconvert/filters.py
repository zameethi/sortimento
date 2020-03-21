import django_filters
from django import forms
from .models import Cruzada
from .models import Sortim



class CruzadaFilter(django_filters.FilterSet):
    Filial = django_filters.NumberFilter(field_name='Filial', lookup_expr='exact', required=True)
    # Cod_Secao = django_filters.NumberFilter(field_name='Cod_Secao')
    # Cod_Secao = django_filters.ChoiceFilter(field_name='Cod_Secao', required=True, choices=[
    #     (d) for d in Sortim.objects.all().values_list('Cod_Secao', 'Desc_Secao').order_by('Desc_Secao').distinct()
    # ], widget=forms.Select(attrs={'style': 'height:30px;width:75%;',}))

    class Meta:
        model = Cruzada
        fields = ['Filial','Cod_Secao']




    def __init__(self, *args, **kwargs):
        super(CruzadaFilter, self).__init__(*args, **kwargs)
        # at sturtup user doen't push Submit button, and QueryDict (in data) is empty
        if self.data == {}:
            self.queryset = self.queryset.none()