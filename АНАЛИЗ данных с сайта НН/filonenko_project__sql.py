#импортируем библиотеки sqlite3 и pandas
import sqlite3
import pandas as pd

#устанавливаем pandas_profiling
!pip install pandas_profiling[notebook]

!pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip

#импортируем pandas_profiling
import pandas_profiling

#готовим датафрейм 'area'с данными
df1=pd.read_excel('/content/area.xlsx')

df1

#проводим анализ-отчет датафрейма 'area' c помощью pandas_profiling
df1.profile_report()

#готовим датафрейм 'employer' с данными
df2=pd.read_excel('/content/employer.xlsx')

df2

#проводим анализ-отчет датафрейма 'employer' с помощью pandas_profiling
df2.profile_report()

# готовим датафрейм 'vacancies_data_for_analysis' с данными
df3=pd.read_excel('/content/vacancies_data_for_analysis.xlsx')

df3

# проводим анализ-отчет датафрейма 'vacancies_data_for_analysis' с помощью pandas_profiling
df3.profile_report()

# удаление дубликатов из датафрейма 'vacancies_data_for_analysis'
df3 = df3.drop_duplicates()

df3

# Определение нужных столбцов и сохранение результатов
df3 = df3[['id', 'name', 'area.id','address.metro.station_name','salary.from','salary.to','address.raw','experience.name','schedule.name','employment.name','employer.id','alternate_url','created_at']]

df3

df3.columns

# повторный анализ-отчет датафрейма 'vacancies_data_for_analysis' с помощью pandas_profiling
df3.profile_report()

# подключение к базе данных, создание новой базы  'vacancies_data_analysis.db'
con=sqlite3.connect('vacancies_data_analуsis.db', timeout=10)
cur=con.cursor()

# загружаем таблицу 'area"  в базу данных
df1.to_sql(con=con, name='area', index=False)

# загружаем таблицу 'employer' в базу данных
df2.to_sql(con=con, name='employer', index=False)

# загружаем таблицу 'vacancies' в базу данных
df3.to_sql(con=con, name='vacancies', index=False)
