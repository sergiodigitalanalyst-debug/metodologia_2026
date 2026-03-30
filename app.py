import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Configuración de página (Pilar: Escalabilidad y Rendimiento)
st.set_page_config(page_title="EcoRide - Intelligence Hub 2026", layout="wide")

st.title("🚀 EcoRide: Business Intelligence & Predictive Hub")
st.markdown("---")

# --- LÓGICA DE NEGOCIO (Fase 03: Transformación) ---
def apply_adstock(spend, decay):
    adstock = np.zeros(len(spend))
    for i in range(len(spend)):
        adstock[i] = spend[i] if i == 0 else spend[i] + decay * adstock[i-1]
    return adstock

# Sidebar para interacción (Fase 05: Activación)
st.sidebar.header("Parámetros de Simulación")
decay_rate = st.sidebar.slider("Tasa de Adstock (Efecto Memoria)", 0.0, 1.0, 0.6)
conversion_lift = st.sidebar.number_input("Ajuste de Incrementalidad (%)", -50, 50, 15)

# --- VISUALIZACIÓN 1: COMPARATIVA ROI (Análisis Causal) ---
st.header("1. Auditoría de Rentabilidad: Causal vs Tradicional")
col1, col2 = st.columns([2, 1])

# Datos simulados basados en nuestra tabla master_atribucion
data_roi = {
    'Canal': ['Paid Search', 'Paid Social', 'SEO', 'Email'],
    'ROI Last-Click': [8.5, 1.2, 2.5, 12.0],
    'ROI Causal (Real)': [3.2, 4.8, 6.1, 2.1]
}
df_roi = pd.DataFrame(data_roi)

with col1:
    fig_roi = px.bar(df_roi, x='Canal', y=['ROI Last-Click', 'ROI Causal (Real)'], 
                     barmode='group', title="Desviación de Atribución",
                     color_discrete_sequence=['#b0bec5', '#1a5f7a'])
    st.plotly_chart(fig_roi, use_container_width=True)

with col2:
    st.write("**Insight Estratégico:**")
    st.info(f"Detectamos una sobrevaloración del {((8.5-3.2)/8.5)*100:.1f}% en Paid Search debido a la Canibalización SEO.")
    st.warning("El Email Marketing actúa como 'recolector', no como generador de demanda primaria.")

# --- VISUALIZACIÓN 2: CANIBALIZACIÓN (Diagnóstico y Predicción) ---
st.header("2. Monitorización de Canibalización SEO/SEM")
# Simulación de serie temporal
dates = pd.date_range(start='2023-01-01', periods=100, freq='W')
sem_spend = np.random.normal(5000, 1000, 100)
seo_sales = 10000 - (sem_spend * 0.24) + np.random.normal(0, 500, 100) # El famoso 24%

fig_cann = go.Figure()
fig_cann.add_trace(go.Scatter(x=dates, y=sem_spend, name="Inversión SEM", line=dict(color='blue')))
fig_cann.add_trace(go.Scatter(x=dates, y=seo_sales, name="Ventas SEO", yaxis="y2", line=dict(color='green')))

fig_cann.update_layout(
    title="Interferencia en el Ecosistema Digital",
    yaxis=dict(title="Gasto SEM (€)"),
    yaxis2=dict(title="Ventas SEO", overlaying="y", side="right")
)
st.plotly_chart(fig_cann, use_container_width=True)

# --- PLAN DE ACTIVACIÓN (Paso 05) ---
st.header("3. Hoja de Ruta Prescriptiva")
st.success("""
- **Inmediato:** Reducir puja en términos de marca (Tasa de sustitución: 24%).
- **Estratégico:** Reasignar 12% del presupuesto a Paid Social para aprovechar la curva de saturación.
- **Técnico:** Mantener la unificación por User ID para evitar silos de información.
""")
