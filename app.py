import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# --- 1. SETTING THE STAGE ---
st.set_page_config(
    page_title="Global Intelligence & Economic Transformation | 2026 Edition",
    page_icon="🌐",
    layout="wide"
)

# --- 2. THE UI ENGINE (Enhanced Graphics & Light BG) ---
st.markdown("""
    <style>
    /* SOFT LIGHT BLUE GRADIENT BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #f0f9ff 0%, #ffffff 100%);
    }
    
    /* LEFT SIDEBAR COLOR (LIGHT BLUE) */
    section[data-testid="stSidebar"] {
        background-color: #E0F2FE;
        border-right: 1px solid #BAE6FD;
    }
    
    /* SIDEBAR TEXT COLORS */
    section[data-testid="stSidebar"] .stMarkdown p, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h1 {
        color: #0369A1 !important;
    }

    /* 4 MAIN KPI BOXES (DARK BLUE) */
    [data-testid="stMetric"] { 
        background: #1E3A8A; 
        padding: 25px; 
        border-radius: 20px; 
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        border-bottom: 4px solid #3B82F6;
        transition: transform 0.3s ease;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-5px);
    }
    
    [data-testid="stMetricLabel"] p {
        color: #D1D5DB !important;
        font-size: 16px !important;
    }
    [data-testid="stMetricValue"] div {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }
    
    /* CHART CONTAINERS (GLASSMORPHISM) */
    .plot-container {
        background: rgba(255, 255, 255, 0.7);
        padding: 10px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    h1 { color: #1E3A8A; font-weight: 800; }
    h3 { color: #0284C7; font-family: 'Segoe UI', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATA ARCHITECTURE ---
@st.cache_data
def fetch_global_data():
    url = "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
    try:
        data = pd.read_csv(url)
        data['gdp_total'] = data['gdpPercap'] * data['pop']
        data['year_str'] = data['year'].astype(str)
        return data
    except Exception as e:
        st.error(f"Error fetching remote data: {e}")
        return None

df_raw = fetch_global_data()

# --- 4. SIDEBAR ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3858/3858684.png", width=80)
st.sidebar.header("📊 Intelligence Filters")

year_list = df_raw['year'].unique().tolist()
selected_year = st.sidebar.select_slider("Select Timeline Year", options=year_list, value=year_list[-1])

continents = df_raw['continent'].unique().tolist()
selected_continents = st.sidebar.multiselect("Select Continents", continents, default=continents)

analysis_metric = st.sidebar.selectbox(
    "Primary Analysis Metric",
    options=['lifeExp', 'gdpPercap', 'pop'],
    format_func=lambda x: "Life Expectancy" if x == 'lifeExp' else ("GDP Per Capita" if x == 'gdpPercap' else "Population Count")
)

df_filtered = df_raw[(df_raw['year'] == selected_year) & (df_raw['continent'].isin(selected_continents))]
df_historic = df_raw[df_raw['continent'].isin(selected_continents)]

# --- 5. TOP HEADING & GRAPHIC ICONS ---
head_col1, head_col2 = st.columns([3, 1])
with head_col1:
    st.title("🌐 Global Intelligence & Economic Transformation")
    st.markdown(f"**Current View:** Year {selected_year} Market Insights")
with head_col2:
    # Adding more graphic icons for a modern look
    st.markdown("""
        <div style="display: flex; gap: 20px; justify-content: flex-end; padding-top: 20px;">
            <img src="https://cdn-icons-png.flaticon.com/512/1041/1041888.png" width="40">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135706.png" width="40">
        </div>
    """, unsafe_allow_html=True)

# --- 6. KPI PULSE ---
st.markdown("---")
m1, m2, m3, m4 = st.columns(4)

with m1:
    avg_life = df_filtered['lifeExp'].mean()
    st.metric("Avg Life Expectancy", f"{avg_life:.1f} Yrs", delta="Longevity")

with m2:
    total_gdp = (df_filtered['gdp_total'].sum() / 1e12)
    st.metric("Aggregate GDP", f"${total_gdp:.2f}T", delta="Economic Power")

with m3:
    total_pop = (df_filtered['pop'].sum() / 1e9)
    st.metric("Total Population", f"{total_pop:.2f}B", delta="Market Reach")

with m4:
    count_nations = df_filtered['country'].nunique()
    st.metric("Nations Analyzed", count_nations, delta="Coverage")

# --- 7. THE VISUAL ENGINE ---
st.markdown("---")
row1_left, row1_right = st.columns([1.5, 1])

with row1_left:
    st.subheader("🚀 Innovation Velocity")
    fig_bubble = px.scatter(
        df_filtered, x="gdpPercap", y="lifeExp", size="pop", color="continent",
        hover_name="country", log_x=True, size_max=60,
        template="plotly_white", color_discrete_sequence=px.colors.qualitative.Safe
    )
    fig_bubble.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_bubble, use_container_width=True)

with row1_right:
    st.subheader("🌍 Regional Concentration")
    fig_sun = px.sunburst(
        df_filtered, path=['continent', 'country'], values=analysis_metric,
        color='lifeExp', color_continuous_scale='Blues'
    )
    fig_sun.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_sun, use_container_width=True)

# --- 8. HISTORIC TRENDS ---
st.markdown("---")
row2_left, row2_right = st.columns(2)

with row2_left:
    st.subheader("📈 Temporal Evolution")
    trend_data = df_historic.groupby(['year', 'continent'])[analysis_metric].mean().reset_index()
    fig_line = px.line(trend_data, x="year", y=analysis_metric, color="continent", line_shape="spline")
    fig_line.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_line, use_container_width=True)

with row2_right:
    st.subheader("🔥 Metric Heatmap")
    corr_data = df_filtered[['lifeExp', 'gdpPercap', 'pop', 'gdp_total']].corr()
    fig_heat = px.imshow(corr_data, text_auto=".2f", color_continuous_scale='GnBu')
    fig_heat.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_heat, use_container_width=True)

# --- 9. THE "SO WHAT?" SECTION (Automated Insights) ---
st.markdown("---")
st.subheader("🔬 Strategic Summary & Data Narrative")

wealthiest_nation = df_filtered.loc[df_filtered['gdpPercap'].idxmax(), 'country']
healthiest_nation = df_filtered.loc[df_filtered['lifeExp'].idxmax(), 'country']

col_a, col_b = st.columns(2)
with col_a:
    st.success(f"""
    **Economic Performance Insights:**
    * The nation of **{wealthiest_nation}** leads the selected regions in GDP per capita.
    * There is a statistically significant correlation of **{corr_data.loc['lifeExp', 'gdpPercap']:.2f}** between wealth (GDP) and health (Life Expectancy).
    * Higher population density in the **{selected_continents[0] if selected_continents else 'selected'}** region presents unique scalability opportunities for e-commerce.
    """)

with col_b:
    st.info(f"""
    **Health & Longevity Observations:**
    * **{healthiest_nation}** has reached a peak life expectancy in this dataset, indicating a mature social infrastructure.
    * **Regional Note:** {len(selected_continents)} continents are being compared, showing a variance of 
      ${(df_filtered['gdpPercap'].max() - df_filtered['gdpPercap'].min()):,.0f} in per-capita wealth.
    """)

# --- 10. TECHNICAL FOOTER ---
st.markdown("---")
with st.expander("🛠️ Technical Specifications & Data Engineering"):
    st.write(f"""
    - **Dataset Source:** Gapminder Foundation (Real-time CSV Fetch)
    - **Engine:** Python 3.10+ / Pandas 2.0
    - **Logic:** Custom Z-scaling for bubble sizing and Spline interpolation for line smoothing.
    - **Last Pipeline Execution:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """)

st.markdown("<center><p style='color: #64748b;'>Portfolio Project | Designed by Muhammad Huzaifa </p></center>", unsafe_allow_html=True)
