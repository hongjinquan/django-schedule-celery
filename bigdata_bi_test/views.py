from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpRequest
from celery_tasks import tasks
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.views.decorators.http import require_GET, require_POST
import json


def task_test_one(request):
    res = tasks.my_taks1.delay(1, 2, 3)
    return HttpResponse(res)


def task_test_two(request):
    tasks.my_task2.delay()
    return HttpResponse("ok")


def task_test_three(request):
    tasks.my_task3.delay()
    return HttpResponse("ok")


@require_GET
def task_test_create(request):
    task_name = request.GET.get("name")
    # tasks.my_task2.delay()
    schedule, create = IntervalSchedule.objects.get_or_create(
        every=10, period=IntervalSchedule.SECONDS)
    print("task_test_create", schedule, create)
    # 创建无参数任务
    ''' PeriodicTask.objects.create(
        interval=schedule, name=task_name, task="celery_tasks.tasks.my_task2") '''
    # 创建有参数任务
    PeriodicTask.objects.create(
        interval=schedule, name=task_name, task="celery_tasks.tasks.my_task3", kwargs=json.dumps({"taskSource": task_name}))
    res = IntervalSchedule.objects.all()
    print("有任务数：", len(res), PeriodicTask.objects.get(name=task_name).enabled)
    return HttpResponse("ok")


@require_GET
def task_test_update(request):
    '''
        修改参数
        1、args: 为list或者元祖，需要json进行序列化为字符串
        2、kwargs: 为dict，需要json进行序列化为字符串
        3、enable: 为bool值，true为启动，false为暂停
    '''
    task_name = request.GET.get("name")
    cur_task = PeriodicTask.objects.get(name=task_name)
    print("cur_task", cur_task)
    cur_task.kwargs = json.dumps({"taskSource": task_name})
    cur_task.save()
    return HttpResponse("ok")


@require_GET
def task_test_stop(request):
    task_name = request.GET.get("name")
    # tasks.my_task2.delay()
    res = IntervalSchedule.objects.all()
    print("有任务数：", len(res), PeriodicTask.objects.get(name=task_name).enabled)

    cur_task = PeriodicTask.objects.get(name=task_name)
    cur_task.enabled = False
    cur_task.save()
    return HttpResponse("stop")


@require_GET
def task_test_restart(request):
    task_name = request.GET.get("name")
    cur_task = PeriodicTask.objects.get(name=task_name)
    cur_task.enabled = True
    cur_task.save()
    return HttpResponse("restart")


@require_GET
def task_test_del(request):
    task_name = request.GET.get("name")
    res = IntervalSchedule.objects.all()
    print("有任务数：", len(res), PeriodicTask.objects.get(name=task_name).enabled)

    cur_task = PeriodicTask.objects.get(name=task_name)
    cur_task.enabled = False
    cur_task.save()
    cur_task.delete()
    return HttpResponse("delete")


@require_GET
def task_nums(request):
    res = PeriodicTask.objects.all()
    print("有任务数：", len(res))
    # for item in res:
    #     print(item)
    return JsonResponse(len(res), safe=False)
