from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpRequest
from celery_tasks import tasks
from django_celery_beat.models import PeriodicTask, IntervalSchedule
schedule, create = IntervalSchedule.objects.get_or_create(
    every=10, period=IntervalSchedule.SECONDS)


def task_test_one(request):
    res = tasks.my_taks1.delay(1, 2, 3)
    return HttpResponse(res)


def task_test_two(request):
    tasks.my_task2.delay()
    return HttpResponse("ok")


def task_test_create(request):
    # tasks.my_task2.delay()
    PeriodicTask.objects.create(
        interval=schedule, name='myTest', task="celery_tasks.tasks.my_task2")
    res = IntervalSchedule.objects.all()
    print("有任务数：", len(res), PeriodicTask.objects.get(name="myTest").enabled)
    return HttpResponse("ok")


def task_test_stop(request):
    # tasks.my_task2.delay()
    res = IntervalSchedule.objects.all()
    print("有任务数：", len(res), PeriodicTask.objects.get(name="myTest").enabled)

    cur_task = PeriodicTask.objects.get(name="myTest")
    cur_task.enabled = False
    cur_task.save()
    return HttpResponse("stop")


def task_test_restart(request):
    cur_task = PeriodicTask.objects.get(name="myTest")
    cur_task.enabled = True
    cur_task.save()
    return HttpResponse("restart")


def task_test_del(request):
    res = IntervalSchedule.objects.all()
    print("有任务数：", len(res), PeriodicTask.objects.get(name="myTest").enabled)

    cur_task = PeriodicTask.objects.get(name="myTest")
    cur_task.enabled = False
    cur_task.save()
    PeriodicTask.objects.get(name = "myTest").delete()
    return HttpResponse("delete")
