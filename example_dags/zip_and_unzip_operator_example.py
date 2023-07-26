from __future__ import print_function
from zip_operator_plugin import ZipOperator, UnzipOperator
from airflow.models import DAG
from datetime import datetime, timedelta
import os

DAG_ID = os.path.basename(__file__).replace(".pyc", "").replace(".py", "")

FILE_TO_ZIP_PATH = "/tmp/input/test.txt"    # location to file or folder to zip
ZIP_FILE_PATH = "/tmp/output/test.txt.zip"  # location save the zip operation to and read the unzip operator from
UNZIP_PATH = "/tmp/output/"                 # location to unzip the contents of the file

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 0,
    }

dag = DAG(DAG_ID, default_args=default_args, schedule_interval=None, start_date=(datetime.now() - timedelta(minutes=1)))

zip_task = ZipOperator(
    task_id='zip_task',
    path_to_file_to_zip=FILE_TO_ZIP_PATH,
    path_to_save_zip=ZIP_FILE_PATH,
    dag=dag)

unzip_task = UnzipOperator(
    task_id='unzip_task',
    path_to_zip_file=ZIP_FILE_PATH,
    path_to_unzip_contents=UNZIP_PATH,
    dag=dag)


zip_task.set_downstream(unzip_task)
