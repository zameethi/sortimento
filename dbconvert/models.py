from django.db import models

# Create your models here.

class Sortemp(models.Model):
    id = models.AutoField(primary_key=True)
    Cod_sortimento = models.CharField(max_length=255, blank=True, null=True)
    Cod_secao = models.CharField(max_length=255, blank=True, null=True)
    Desc_secao = models.CharField(max_length=255, blank=True, null=True)
    Cod_tamanho = models.CharField(max_length=255, blank=True, null=True)
    Desc_tamanho = models.CharField(max_length=255, blank=True, null=True)
    Cod_publico = models.CharField(max_length=255, blank=True, null=True)
    Desc_publico = models.CharField(max_length=255, blank=True, null=True)
    Cod_mercadoria = models.CharField(max_length=255, blank=True, null=True)
    Desc_mercadoria = models.CharField(max_length=255, blank=True, null=True)
    Merc_conj = models.CharField(max_length=255, blank=True, null=True)
    Prioridade = models.CharField(max_length=255, blank=True, null=True)
    Qtde = models.CharField(max_length=255, blank=True, null=True)
    Voltagem = models.CharField(max_length=255, blank=True, null=True)
    Vigencia_inicio = models.DateField(blank=True, null=True)
    Vigencia_fim = models.DateField(blank=True, null=True)
    Status = models.CharField(max_length=2, blank=True, null=True)
    Setor = models.CharField(max_length=255, blank=True, null=True)
    Desc_setor = models.CharField(max_length=255, blank=True, null=True)
    Classe = models.CharField(max_length=255, blank=True, null=True)
    Desc_classe = models.CharField(max_length=255, blank=True, null=True)
    Especie = models.CharField(max_length=255, blank=True, null=True)
    Desc_especie = models.CharField(max_length=255, blank=True, null=True)
    Marca = models.CharField(max_length=255, blank=True, null=True)
    Desc_marca = models.CharField(max_length=255, blank=True, null=True)


class Sortim(models.Model):
    id = models.AutoField(primary_key=True)
    Empresa = models.CharField(max_length=255, blank=True, null=True)
    Filial = models.CharField(max_length=255, blank=True, null=True)
    Voltagem = models.CharField(max_length=255, blank=True, null=True)
    Cod_Publico = models.CharField(max_length=255, blank=True, null=True)
    Desc_Publico = models.CharField(max_length=255, blank=True, null=True)
    Cod_Secao = models.CharField(max_length=255, blank=True, null=True)
    Desc_Secao = models.CharField(max_length=255, blank=True, null=True)
    Cod_Sortimento = models.CharField(max_length=255, blank=True, null=True)
    Cod_Tamanho = models.CharField(max_length=255, blank=True, null=True)
    Desc_Tamanho = models.CharField(max_length=255, blank=True, null=True)
    Tipo_Publico = models.CharField(max_length=255, blank=True, null=True)
    Solic_Volt_Dif = models.CharField(max_length=255, blank=True, null=True)


class Cruzada(models.Model):
    id = models.IntegerField(primary_key=True)
    Cod_sortimento = models.CharField(max_length=255, blank=True, null=True)
    Cod_mercadoria = models.CharField(max_length=255, blank=True, null=True)
    Desc_mercadoria = models.CharField(max_length=255, blank=True, null=True)
    Prioridade = models.CharField(max_length=255, blank=True, null=True)
    Voltagem_item = models.CharField(max_length=255, blank=True, null=True)
    Voltagem_filial = models.CharField(max_length=255, blank=True, null=True)
    Vigencia_inicio = models.DateField(blank=True, null=True)
    Vigencia_fim = models.DateField(blank=True, null=True)
    Status = models.CharField(max_length=2, blank=True, null=True)
    Filial = models.IntegerField(blank=True, null=True)
    Cod_Secao = models.IntegerField(blank=True, null=True)
    Desc_Secao = models.CharField(max_length=255, blank=True, null=True)
    Cod_Tamanho = models.CharField(max_length=255, blank=True, null=True)
    Desc_Tamanho = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "cruzada"


class Tamanhos(models.Model):
    Tamanho = models.CharField(max_length=20)
    Tipo = models.CharField(max_length=20)


class Perfil(models.Model):
    Nome = models.CharField(max_length=100)
    Tamanho = models.ForeignKey(Tamanhos, on_delete=models.CASCADE)


class Secao(models.Model):
    Cod_secao = models.IntegerField(primary_key=True)
    Descricao = models.CharField(max_length=255)


class Classificacao(models.Model):
    cod_secao = models.ForeignKey(Secao, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    Quantidade = models.IntegerField()
