from kombu import Exchange, Queue

BROKER_URL = 'amqp://guest:123456@127.0.0.1:15672/'  # 使用amqp作为消息代理
# BROKER_URL = 'redis://127.0.0.1:6378/2'  # 使用redis作为消息代理

RESULT_BROKER_TRANSPORT_OPTIONS = {"master_name": "mymaster"}

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'  # 把任务结果存在了Redis

# redis集群哨兵模式---------------
# CELERY_RESULT_BACKEND = 'sentinel://10.237.102.210:26379/4;' \
#                         'sentinel://10.237.102.211:26379/4;' \
#                         'sentinel://10.237.102.212:26379/4'
# BROKER_URL = 'sentinel://10.237.102.210:26379/3;' \
#              'sentinel://10.237.102.211:26379/3;' \
#              'sentinel://10.237.102.212:26379/3'
#
# BROKER_TRANSPORT_OPTIONS = {
#     'master_name': 'mymaster',
#     'service_name': 'mymaster',
#     'socket_timeout': 6000,
#     'visibility_timeout': 3600,
# }
# CELERY_RESULT_BACKEND_TRANSPORT_OPTIONS = BROKER_TRANSPORT_OPTIONS
#  redis集群哨兵模式---------------


IMPORTS = ("celery_test.celery_app_task",)
task_name_list = ['task_A', 'task_B', 'task_C', 'task_D']

CELERY_QUEUES = (
    Queue("for_task_A", Exchange("for_task_A"), routing_key="for_task_A"),
    Queue("for_task_B", Exchange("for_task_B"), routing_key="for_task_B"),
    Queue("for_task_C", Exchange("for_task_C"), routing_key="for_task_C"),
    Queue("for_task_D", Exchange("for_task_D"), routing_key="for_task_D")
)

CELERY_ROUTES = (
    {
        "celery_test.celery_app_task.taskA":
            {
                'queue': "for_task_A",
                "routing_key": "for_task_A"
            },
    },

    {
        "celery_test.celery_app_task.taskB":
            {
                'queue': "for_task_B",
                "routing_key": "for_task_B"
            },
    },

    {
        "celery_test.celery_app_task.taskC":
            {
                'queue': "for_task_C",
                "routing_key": "for_task_C"
            },
    },
    {
        "celery_test.celery_app_task.taskD":
            {
                'queue': "for_task_D",
                "routing_key": "for_task_D"
            },
    },
)

CELERY_TASK_SERIALIZER = 'msgpack'  # 任务序列化和反序列化使用msgpack方案
# CELERY_TASK_SERIALIZER = 'json'  # 任务序列化和反序列化使用msgpack方案

CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON

CELERY_TASK_RESULT_EXPIRES = 60*24  # 任务过期时间（秒）

CELERY_ACCEPT_CONTENT = ['json', 'msgpack']  # 指定接受的内容类型

CELERY_REJECT_ON_WORKER_LOST = True  # 当worker进程意外退出时，task会被放回到队列中
CELERY_ACKS_LATE = True  # 只有当worker完成了这个task时，任务才被标记为ack状态

# 并发数
CELERYD_CONCURRENCY = 2

