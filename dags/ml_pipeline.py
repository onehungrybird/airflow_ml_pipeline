from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

import sys

# Add the 'scripts' directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "scripts"))

from download_data import download_data
from train_model import train_model
from evaluate_model import evaluate_model


# Define DAG arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define DAG
dag = DAG(
    'ml_pipeline',
    default_args=default_args,
    description='End-to-end ML pipeline with Airflow',
    schedule_interval='@daily',  # Runs daily
    catchup=False
)

# Define tasks
task_download = PythonOperator(
    task_id='download_data',
    python_callable=download_data,
    dag=dag
)

task_train = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag
)

task_evaluate = PythonOperator(
    task_id='evaluate_model',
    python_callable=evaluate_model,
    dag=dag
)

# Define task dependencies
task_download >> task_train >> task_evaluate
