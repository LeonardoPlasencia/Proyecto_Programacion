import pandas as pd
import streamlit as st
import numpy as np
st.title('Datos positivos Covid-19')
st.write('Esta es una web donde podrá visualizar casos positvos de covid-19 por ubicación, sexo, edad, etc.')

#dataset_link = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'

###Hay que obtener la data de un link

#df = pd.read_csv(dataset_link, header=None) ###Lee el dataframe respectivo

df = pd.read_csv(r'C:/Users/Leonardo/Downloads/positivos_covid.csv',sep=";", skip_blank_lines=True, date_parser=True)

from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
count_sex=df["SEXO"].value_counts().FEMENINO
count_sexM=df["SEXO"].value_counts().MASCULINO
metodo_A=df["METODODX"].value_counts().PCR
metodo_B=df["METODODX"].value_counts().AG
b = (
   Bar()
    .add_xaxis(["Femenino", "Masculino", "PCR", "AG"])
    .add_yaxis(
        "Sexo y tipo de prueba aplicada", [int(count_sex), int(count_sexM), int(metodo_A), int(metodo_B)]
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Datos", subtitle="Sexo y métodos"
        )#,
        #toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(b)
