"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2017, 11, 9),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    'end_date': datetime(2017, 11, 20),
}

dag = DAG(
    'first_dag', default_args=default_args, schedule_interval='*/1 * * * *')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='update_tag_t1',
    bash_command='python /Users/zhaoyongqiang/workspace/v12/t.py',
    dag=dag)

t2 = BashOperator(
    task_id='update_tag_t2',
    bash_command='python /Users/zhaoyongqiang/workspace/v12/t2.py',
    dag=dag)

t2.set_upstream(t1)
