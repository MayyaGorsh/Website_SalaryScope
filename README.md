# Website SalaryScope

This project presents a **data analysis of salary trends** across various categories and macroeconomic indicators.

The project is structured in two main stages:

- **Stage 1**: Data analysis and visualization in Jupyter Notebook (`analytics` folder)  
- **Stage 2**: Development of an **interactive web application** using **Streamlit** (`app` folder)  

![image](https://github.com/user-attachments/assets/4deb5050-66eb-49fa-bca7-6ba7895e7180)

## Data Sources

The data was obtained from the following official sources and processed in the notebook under `analytics`:

- [Federal State Statistics Service (Rosstat)](https://rosstat.gov.ru/labor_market_employment_salaries)  
- [Inflation Portal](https://xn----ctbjnaatncev9av3a8f8b.xn--p1ai/)  
- [Russian Public Opinion Research Center (WCIOM)](https://wciom.ru/analytical-reviews/analiticheskii-obzor/schaste-v-rossii-monitoring-16042025)  
- [Exchange Rates Archive](https://ru.myfin.by/currency/cb-rf-archive/usd)

---

## App Launch

Access the deployed app here:  
**[Streamlit App](https://mvp-in-data-science-mayya-gorsh-salary-statictics.streamlit.app/)**

To run locally:

```bash
pip install -r requirements.txt
streamlit run app/app.py
```
