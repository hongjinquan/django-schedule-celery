from celery import shared_task


@shared_task
def my_taks1(a, b, c):
    print("任务my_taks1函数正在执行.....")
    return a + b + c


@shared_task
def my_task2():
    print("任务my_task2函数正在执行.....")


@shared_task
def my_task3(taskSource):
    print("任务my_task3函数正在执行.....", taskSource)
