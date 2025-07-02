# Website SalaryScope

This project presents a **data analysis of salary trends** across various categories and macroeconomic indicators.

The project is structured in two main stages:

- **Stage 1**: Data analysis and visualization in Jupyter Notebook (`analytics` folder)  
- **Stage 2**: Development of an **interactive web application** using **Streamlit** (`app` folder)  

The datasets used for analysis are stored in the `data` folder.

## Data Sources

The data was obtained from the following official sources and processed in the notebook under `analytics`:

- [Federal State Statistics Service (Rosstat)](https://rosstat.gov.ru/labor_market_employment_salaries)  
- [Inflation Portal](https://xn----ctbjnaatncev9av3a8f8b.xn--p1ai/)  
- [Russian Public Opinion Research Center (WCIOM)](https://wciom.ru/analytical-reviews/analiticheskii-obzor/schaste-v-rossii-monitoring-16042025)  
- [Exchange Rates Archive](https://ru.myfin.by/currency/cb-rf-archive/usd)

---

## App Launch

Access the deployed app here:  
**[task_analytics Streamlit App](https://mvp-in-data-science-mayya-gorsh-salary-statictics.streamlit.app/)**

To run locally:

```bash
pip install -r requirements.txt
streamlit run app/app.py
```