import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Путь к корню репозитория
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

df_salary = pd.read_csv(os.path.join(BASE_DIR, 'data', 'salary_data_longer_full.csv'))
df_macro = pd.read_csv(os.path.join(BASE_DIR, 'data', 'macro_data.csv'))
df_events = pd.read_csv(os.path.join(BASE_DIR, 'data', 'events.csv'))

st.title("Динамика заработной платы и макроэкономических параметров")

# Выбор отраслей
categories = df_salary['Категория'].unique()
selected_categories = st.multiselect("Выберите отрасли", categories, default=categories[20])

# Выбор макропараметра
macro_options = ['Не показывать', 'Инфляция', 'ВВП на душу', 'USD', 'Прибывшие', 'Уехавшие', 'Индекс счастья']
selected_macro = st.selectbox("Выберите макропоказатель", macro_options)

# Отображение базовой зарплаты
show_baseline = st.checkbox("Показывать базовую зарплату", value=True)

# Отображение событий
show_events = st.checkbox("Показывать важные события", value=False)

# Строим график
fig, ax1 = plt.subplots(figsize=(16, 9))

colors = plt.cm.tab10.colors

# Первая ось — заработная плата
for idx, category in enumerate(selected_categories):
    subset = df_salary[df_salary['Категория'] == category]
    color = colors[idx % len(colors)]

    ax1.plot(subset['Год'], subset['Реальная зарплата'], label=f"{category} (реальная)",
             marker='o', linewidth=2, color=color)

    if show_baseline:
        ax1.plot(subset['Год'], subset['Базовая зарплата'], linestyle='--', linewidth=2, color=color)

ax1.set_xlabel("Год")
ax1.set_ylabel("Заработная плата")
ax1.legend(loc='upper left')
ax1.grid(True)
plt.figtext(0.5, -0.05,
             'Пунктирные линии показывают уровень зарплаты, скорректированный на инфляцию (базовая зарплата)',
             ha='center', fontsize=10)
# Вторая ось — макропоказатель
if selected_macro != 'Не показывать':
    ax2 = ax1.twinx()
    # 3 строки чтобы макро был за зарплатами
    ax2.set_zorder(1)
    ax1.set_zorder(2)
    ax1.patch.set_alpha(0)
    macro_column_map = {
        'Инфляция': 'Инфляция',
        'ВВП на душу': 'ВВП на душу',
        'USD': 'USD',
        'Прибывшие': 'Прибывшие',
        'Уехавшие': 'Уехавшие',
        'Индекс счастья': 'Индекс счастья'
    }
    macro_column = macro_column_map[selected_macro]

    ax2.step(df_macro['Год'], df_macro[macro_column], color='gray', linewidth=0.5, where='mid')
    ax2.fill_between(df_macro['Год'], df_macro[macro_column], step='mid', color='lightgray', alpha=0.5)
    ax2.set_ylabel(selected_macro)

# Добавляем события как красные точки с подписями
# Добавляем события как вертикальные линии с подписями
if show_events:
    for _, row in df_events.iterrows():
        event_year = row['Год']
        event_label = row['Событие']
        ax1.axvline(x=event_year, color='black', linestyle='-', linewidth=1, zorder=3)
        mid_y = (ax1.get_ylim()[0] + ax1.get_ylim()[1]) / 2 # середина оси у
        ax1.text(event_year + 0.2,
                 mid_y,
                 event_label,
                 rotation=90,
                 verticalalignment='center',
                 horizontalalignment='left',
                 fontsize=8,
                 color='black',
                 zorder=3)

st.pyplot(fig)
