import streamlit as st
import pandas as pd
import gdown

from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

st.title("Proyecto Programación")

#id = 1op-iq0XhBXBQOPlagCPE9TzFsFkkNVjQ
@st.experimental_memo
def download_data():
  #https://drive.google.com/uc?id=
  url = "https://drive.google.com/uc?id=1op-iq0XhBXBQOPlagCPE9TzFsFkkNVjQ"
  output= "data.csv"
  gdown.download(url,output,quiet = False)
  
download_data()
data = pd.read_csv("data.csv", sep = ";", parse_dates = ["FECHA_CORTE","FECHA_RESULTADO"])
Simplificado = data.drop(columns = ["DISTRITO","FECHA_CORTE","FECHA_RESULTADO","UBIGEO","id_persona"])

count_sex=Simplificado["SEXO"].value_counts().FEMENINO
count_sexM=Simplificado["SEXO"].value_counts().MASCULINO
metodo_A=Simplificado["METODODX"].value_counts().PCR
metodo_B=Simplificado["METODODX"].value_counts().AG
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
