# 🌐 Global Intelligence Hub | Executive Economic Insights 2026
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Latest-507282?logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green)

###  [View Live Dashboard Here](https://global-intelligence-economic-transformation-d5qpfkjpfnsgcrpc9d.streamlit.app/)

An advanced, interactive Business Intelligence (BI) engine designed to visualize global transformation through the lens of wealth, health, and population dynamics. This project leverages real-world data from the **Gapminder Foundation** to provide executive-level insights into market scalability and economic longevity.

---

## 📊 Key Dashboard Features
* **Dynamic Intelligence Filters:** Multi-regional and temporal selection (1952–2026) for granular trend analysis.
* **Innovation Velocity Engine:** A 4D Bubble Chart visualizing the correlation between GDP Per Capita and Life Expectancy.
* **Hierarchical Regional Concentration:** Sunburst visualizations detailing economic density by continent and country.
* **Statistical Deep-Dives:** Automated correlation heatmaps and temporal spline-interpolated line charts.
* **Automated Narrative Generation:** Real-time business insights generated based on filtered data parameters.

---

## 🛠️ Tech Stack & Data Engineering
* **Frontend:** Streamlit (Custom CSS/Glassmorphism UI)
* **Data Processing:** Pandas (Feature Engineering & Z-Score Anomaly Detection)
* **Visuals:** Plotly Express & Graph Objects (Interactive SVG/HTML exports)
* **Architecture:** Cached Data Ingestion Pipeline (`@st.cache_data`) for high-speed performance.

### Data Cleaning & Logic
> "Raw data was ingested via a secure SSL-verified endpoint. Feature engineering was applied to calculate `Aggregate GDP` ($GDP \times Population$) and `Growth Multipliers` to normalize skewed economic distributions."

---

## 📸 Dashboard Interface
<p align="center">
  <img src="https://raw.githubusercontent.com/streamlit/docs/main/public/images/tutorials/create-a-data-explorer-app.png" width="800" alt="Dashboard Preview">
</p>

---

## 📂 Project Structure
```text
├── app.py              # Main Streamlit application
├── requirements.txt    # Production dependencies
├── global_data.csv     # Local backup of the Gapminder dataset
└── README.md           # Technical documentation
