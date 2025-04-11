import numpy as np
import streamlit as st
from documento_mestre import master_internal_fuses

st.title("Cálculos de desbalanceamento para um banco de capacitores conectado em duplo Y")
st.image("Figure 34 Illustration of an uneven double wye connected bank.png")

# Criar cinco colunas
col1, col2, col3, col4, col5 = st.columns(5)

# Coluna 1
with col1:
    S = st.number_input(
        label="Quantidade Série de Unidades - S:",
        min_value=1,
        max_value=20,
        value=3,
        step=1,
        format="%d"
    )
    Pt = st.number_input(
        label="Total de Unidades Paralelas - Pt:",
        min_value=1,
        max_value=60,
        value=2,
        step=1,
        format="%d"
    )

# Coluna 2
with col2:
    Pa = st.number_input(
        label="Unidades Paralelas da Fase Afetada - Pa:",
        min_value=1,
        max_value=10,
        value=1,
        step=1,
        format="%d"
    )
    P = st.number_input(
        label="Unidades Paralelas na String Afetada - P:",
        min_value=1,
        max_value=10,
        value=1,
        step=1,
        format="%d"
    )

# Coluna 3
with col3:
    G = st.number_input(
        label="Aterrado (0) Isolado (1) - G:",
        min_value=0,
        max_value=1,
        value=1,
        step=1,
        format="%d"
    )
    N = st.number_input(
        label="Paralelos dentro da Unidade - N:",
        min_value=1,
        max_value=30,
        value=9,
        step=1,
        format="%d"
    )

# Coluna 4
with col4:
    Su = st.number_input(
        label="Elementos em Série - Su:",
        min_value=1,
        max_value=20,
        value=6,
        step=1,
        format="%d"
    )
    f1 = st.number_input(
        label="Frequência Fundamental - Hz:",
        min_value=40,
        max_value=70,
        value=60,
        step=1,
        format="%d"
    )

# Coluna 5
with col5:
    power_bank_rated = 1e6 * st.number_input(
        label="Potência Nominal do Banco - MVAr:",
        min_value=0.001,
        max_value=100.0,
        value=6.952,
        step=0.1,
        format="%.2f"
    )
    voltage_bank_rated = 1e3 * st.number_input(
        label="Tensão Nominal do Banco - kV:",
        min_value=1.0,
        max_value=1000.0,
        value=54.800,
        step=0.1,
        format="%.2f"
    )

    voltage_bank_work = 1e3 * st.number_input(
        label="Tensão de Trabalho do Banco - kV:",
        min_value=1.0,
        max_value=1000.0,
        value=34.5,
        step=0.1,
        format="%.2f"
    )



df_stylized, trip_current_max, trip_voltage_max = \
    master_internal_fuses(f1=f1,
                          power_bank_rated=power_bank_rated,
                          voltage_bank_rated=voltage_bank_rated,
                          voltage_bank_work = voltage_bank_work,
                          S=S, Pt=Pt, Pa=Pa, P=P, G=G, N=N, Su=Su)

st.dataframe(df_stylized)
st.write(f"Máxima Corrente Entre Estrelas = {trip_current_max} A")
st.write(f"Máxima Tensão de Deslocamento de Neutro = {trip_voltage_max} V")
