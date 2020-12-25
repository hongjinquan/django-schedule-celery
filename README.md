# django-schedule-celery
> 结合django和celery的动态添加任务，实现任务调度


### celery 任务配置
> 请查看项目中的celery_tasks中项目代码

### 集成到django
> 请查看项目中bigdata_bi_test中的settings配置

### 项目启动时加载celery实例
> 请查看项目中bigdata_bi_test中的__init__.py 文件

```
from celery_tasks.celeryapp import app as celery_app
__all__ = ('celery_app',)
```

### supervisord 启动
> 请查看 supervisord.conf 的配置

### 项目启动
1. 数据库实例生成：python manager.py migrate
1. django项目启动：python manager.py runserver
2. celery管理器启动：supervisord -c ./supervisord.conf