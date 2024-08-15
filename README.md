# Data-Engineer-Projects

## В репозитории хранятся проекты, выполненные по направлению Data Engineer (Дата-инженер).
#### Источники данных не приложены.

|   № |    Название проекта  |   Описание |  Навыки и инструменты |
|:----|:---------------------|:---------|:----------------------|
|   1.  |     [Link](Разработка телеграмм-бота.)                 |    С использованием Python, разработан телеграмм-бот, который позволил переводить слова, выражения, предложения с русского на английский и с английского на русский.      |   Python (библиотеки: Telebot, Googletrans), Pycharm (среда разработки).                    |
|   2.  |     АНАЛИЗ данных с сайта НН.                 |   Провести анализ вакансии по специализации аналитика данных на основе файлов с выгрузкой данных с сайта headhunter, получив ответы на поставленные вопросы.      |   Python (библиотеки: Pandas). SQL. Google Colab. DBeaver/SQLite. Draw.io.                    |  
|   3.  |     ЗАГРУЗКА ДАННЫХ из API в DWH.                 |   1. В "ручном" режиме: Получить "сырые" данные из API и сохранить их в MinioS3 в форматах json и parquet. Из MinioS3 загрузить данные в формате parquet в DWH, во временные таблицы GreenPlum. И в заключении из временных таблиц загрузить данные в спроектированные объекты Data Vault. 2. С помощью Аpache Airflow объединить все этапы в один общий, непрерывный поток, конвейер данных.      |   Python (библиотеки: requests, boto3, json, pandas, pyarrow). SQL. Командная строка Linux. Docker compose. Minio. Greenplum. DBT. Data Vault 2.0. Apache Airflow. VSCode. Draw.io. DBeaver.
|   4.  |     ЗАГРУЗКА ДАННЫХ, из Hadoop (HDFS), Apache Kafka  с использованием Apache Spark в Hadoop (HDFS).                 |   Подготовить данные в HDFS. Загрузить данные в топик Apache Kafka. Переписать запрос для сборки витрины с SQL на PySpark. Сформировать пайплайн, считывая Apache Spark-ом данные из HDFS и из Apache Kafka. Сохранить результат работы пайплайна каждую минуту в формате parquet в произвольную HDFS-директорию.      |   Python (библиотеки: Telebot, Googletrans), Pycharm (среда разработки).**Bold** *Italic* ~~Strike~~ [Link](dot.com)
