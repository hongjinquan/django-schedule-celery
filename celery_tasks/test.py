from tasks import my_task

res = my_task.delay(1, 2)

print(res)
