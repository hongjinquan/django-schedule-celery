from celery_tasks.celeryapp import app

@app.task
def my_taks1(a, b, c):
    print("任务my_taks1函数正在执行.....")
    return a + b + c


@app.task
def my_task2():
    print("任务my_task2函数正在执行....., 任务数量：")
