from datetime import datetime
from airflow import DAG
from airflow.decorators import task

with DAG(
    dag_id = 'try',
    description = 'new dag',
    schedule_interval = "@daily",
    start_date=datetime(2022,11,9),
    catchup=False,
    tags=['example'],
) as dag:

    ## specific tasks
    @task(task_id="try_hello")
    def prints_helloworld():
        print('hello world')
        #return "hello world"

    prints_helloworld()
