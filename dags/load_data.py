from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "Amanuel",
    "email": ["amanuelzewdu21@gmail.com"],
    "email_on_failure": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

dag_exec_scripts = DAG(
    dag_id="loaddata",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=30),
    description="adds data into table and loads it to postgres",
)

create_table = PostgresOperator(
    sql="sql/create_table.sql",
    task_id="createtable_task",
    postgres_conn_id="postgres_dwh",
    dag=dag_exec_scripts,
)

load_data = PostgresOperator(
    sql="sql/load_data.sql",
    task_id="load_data_task",
    postgres_conn_id="postgres_dwh",
    dag=dag_exec_scripts,
)

create_table >> load_data