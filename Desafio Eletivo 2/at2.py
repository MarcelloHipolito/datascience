import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats

# =================== CONFIGURAÇÃO =================== 
st.set_page_config(
    layout="wide",
    page_title="Análise Estatística",
    page_icon="📊"
)

# =================== DADOS =================== 
grupo_a = np.array([3, 5, 7, 9, 11])
grupo_b = np.array([2, 4, 6, 8, 10])
df = pd.DataFrame({'Grupo A': grupo_a, 'Grupo B': grupo_b})

# =================== ESTILO (APLICADO A TODOS EXCETO NORMALIDADE) =================== 
st.markdown("""
<style>
    .metric-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid #4ECDC4;
    }
    .correlacao-box {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# =================== CABEÇALHO =================== 
st.title("📊 Análise Completa: Grupo A vs Grupo B")
st.markdown("---")

# =================== SEÇÃO 1: DADOS BRUTOS ===================
st.header("📋 Dados Brutos")
col_raw1, col_raw2 = st.columns(2)
with col_raw1:
    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
    st.subheader("Grupo A")
    st.dataframe(pd.DataFrame(grupo_a, columns=['Valores']), hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_raw2:
    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
    st.subheader("Grupo B")
    st.dataframe(pd.DataFrame(grupo_b, columns=['Valores']), hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =================== SEÇÃO 2: ESTATÍSTICAS =================== 
st.header("📌 Estatísticas Descritivas")
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
    st.write("**Grupo A**")
    st.write(f"Média: `{np.mean(grupo_a):.2f}`")
    st.write(f"Mediana: `{np.median(grupo_a):.2f}`")
    st.write(f"Desvio Padrão: `{np.std(grupo_a, ddof=1):.2f}`")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
    st.write("**Grupo B**")
    st.write(f"Média: `{np.mean(grupo_b):.2f}`")
    st.write(f"Mediana: `{np.median(grupo_b):.2f}`")
    st.write(f"Desvio Padrão: `{np.std(grupo_b, ddof=1):.2f}`")
    st.markdown('</div>', unsafe_allow_html=True)

# =================== SEÇÃO 3: TESTE DE NORMALIDADE =================== 
st.header("📝 Teste de Normalidade (Shapiro-Wilk)")
shapiro_a = stats.shapiro(grupo_a)
shapiro_b = stats.shapiro(grupo_b)

st.write(f"""
- **Grupo A**: 
  W = `{shapiro_a.statistic:.4f}`, 
  p = `{shapiro_a.pvalue:.4f}`  
  {"✅ Normal" if shapiro_a.pvalue > 0.05 else "❌ Não normal"}
  
- **Grupo B**: 
  W = `{shapiro_b.statistic:.4f}`, 
  p = `{shapiro_b.pvalue:.4f}`  
  {"✅ Normal" if shapiro_b.pvalue > 0.05 else "❌ Não normal"}
""")

# =================== SEÇÃO 4: CORRELAÇÃO =================== 
st.header("🔗 Correlação entre Grupos")
corr, p_val = stats.pearsonr(grupo_a, grupo_b)

st.markdown('<div class="correlacao-box">', unsafe_allow_html=True)
st.write(f"""
**Coeficiente de Pearson:**  
r = `{corr:.4f}`  

**Valor-p:**  
`{p_val:.4f}`  

**Interpretação:**  
{"Correlação perfeita positiva (r = +1)" if corr == 1 else "Correlação positiva forte"}
""")
st.markdown('</div>', unsafe_allow_html=True)

# =================== SEÇÃO 5: GRÁFICOS =================== 
st.header("📈 Visualizações", divider='rainbow')

tab1, tab2 = st.tabs(["Gráfico de Dispersão", "Boxplot"])

with tab1:
    fig1 = px.scatter(
        df, x='Grupo A', y='Grupo B',
        trendline='ols',
        color_discrete_sequence=['#FF6B6B'],
        title='Correlação entre Grupo A e Grupo B',
        width=800, height=500
    )
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    fig2 = px.box(
        pd.melt(df, var_name='Grupo', value_name='Valor'),
        x='Grupo', y='Valor',
        color='Grupo',
        color_discrete_sequence=['#4ECDC4', '#FF6B6B'],
        title='Distribuição dos Valores'
    )
    st.plotly_chart(fig2, use_container_width=True) 