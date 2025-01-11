from airflow.decorators import dag, task
from datetime import datetime
from Bikroy_Dag.src.getMobileData import process_mobiles
from Bikroy_Dag.src.checkMongoForDuplicates import check_mongo_for_duplicates
from Bikroy_Dag.src.uploadToMongo import upload_to_mongo

@dag(
        dag_id="BikroyMobileDag",
        schedule_interval="*/5 * * * *",
        start_date=datetime(2022, 1, 1), 
        catchup=False,
        tags=["Bikroy.com", "Mobile_data"]
    )
def bikroy_mobile_dag():

    @task(task_id="get_mobile_data")
    def get_mobile_data_task():
        process_mobiles()

    @task(task_id="check_mongo_for_duplicates")
    def check_mongo_for_duplicates_task():
        check_mongo_for_duplicates()

    @task(task_id="upload_to_mongo")
    def upload_to_mongo_task():
        upload_to_mongo()

    task1 = get_mobile_data_task()
    task2 = check_mongo_for_duplicates_task()
    task3 = upload_to_mongo_task()

    task1 >> task2>> task3

dag = bikroy_mobile_dag()