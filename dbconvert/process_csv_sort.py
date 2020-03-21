import csv
import os
import pandas
from django.db.models import Q
from .models import Sortemp
import sqlite3
from datetime import datetime
# from django.db import connection
import psycopg2 as pg
import pandas.io.sql as psql
from sqlalchemy import create_engine
from django.conf import settings

base_dir = settings.BASE_DIR
static = settings.STATIC_ROOT

def importar_csv():
    path = '{}\\files\\QUERY SORTIMENTO SEÇÃO MOVEIS 2.csv'.format(static)
    with open(path) as f:
        a = sum(1 for line in f)

    with open(path) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for n, row in enumerate(reader):
            for k, i in row.items():
                if i == "None":
                    row[k] = None
            p = Sortemp(Cod_sortimento=row['COD SORTIMENTO'], Cod_secao=row['COD SECAO'], Desc_secao=row['DESC SECAO'],
                        Cod_tamanho=row['COD TAMANHO'], Desc_tamanho=row['DESC TAMANHO'], Cod_publico=row['COD PUBLICO'],
                        Desc_publico=row['DESC PUBLICO'], Cod_mercadoria=row['COD MERCADORIA'], Desc_mercadoria=row['DESC MERCADORIA'],
                        Merc_conj=row['MERC / CONJ'], Prioridade=row['PRIORIDADE'], Qtde=row['QTDE'], Voltagem=row['VOLTAGEM'],
                        Vigencia_inicio=row['VIGENCIA INICIO'], Vigencia_fim=row['VIGENCIA FIM'], Status=row['STATUS'],
                        Setor=row['SETOR'], Desc_setor=row['DESC SETOR'], Classe=row['CLASSE'], Desc_classe=row['DESC CLASSE'],
                        Especie=row['ESPECIE'], Desc_especie=row['DESC ESPECIE'], Marca=row['MARCA'], Desc_marca=row['DESC MARCA'])
            p.save()
            print(f"processando {n} de {a}")

def csv_pandas():
    path = '{}\\files'.format(static)
    # sql1 = 'DELETE FROM dbconvert_sortemp'
    # sql2 = 'DELETE FROM dbconvert_sortim'
    # cur = connection.cursor()
    # cur.execute(sql1)
    # cur.execute(sql2)
    # cur.commit()
    sortemp_arqs = []
    sortim_arqs = []

    # con = sqlite3.connect("db.sqlite3")
    # con = pg.connect("host='localhost' dbname=sortimento user=django password='123'")

    con = create_engine('postgresql://django:123@localhost:5432/sortimento')

    lista_arqs = [arq for arq in os.listdir(path)]
    for i in lista_arqs:
        if 'SORTIM.csv' in i:
            sortim_arqs.append("{}\\{}".format(path, str(i).replace(']','').replace('[','').replace("'",'')))
        else:
            sortemp_arqs.append("{}\\{}".format(path, str(i).replace(']','').replace('[','').replace("'",'')))
    for files in sortemp_arqs:
        df = pandas.read_csv(files, sep=';',encoding='ISO-8859-1', low_memory=False, index_col=False)
        df.columns = ('Cod_sortimento','Cod_secao','Desc_secao','Cod_tamanho','Desc_tamanho','Cod_publico','Desc_publico','Cod_mercadoria','Desc_mercadoria','Merc_conj','Prioridade','Qtde','Voltagem','Vigencia_inicio','Vigencia_fim','Status','Setor','Desc_setor','Classe','Desc_classe','Especie','Desc_especie','Marca','Desc_marca')
        psql.to_sql('dbconvert_sortemp', con, if_exists='append', chunksize=1000, index_label='id')

    for files in sortim_arqs:
        df = pandas.read_csv(files, sep=';',encoding='ISO-8859-1', low_memory=False, index_col=False)
        df.columns = ('Empresa','Filial','Voltagem','Cod_Publico','Desc_Publico','Cod_Secao','Desc_Secao','Cod_Sortimento','Cod_Tamanho','Desc_Tamanho','Tipo_Publico','Solic_Volt_Dif')

        psql.to_sql(df,'dbconvert_sortim', con, chunksize=1000, index_label='id',schema='public',if_exists='replace')


    return df.head()

def teste1():
    orm = Sortemp.objects.filter(Q(name__contains='a'))