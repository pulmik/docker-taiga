from kombu import Queue

broker_url = 'amqp://taiga:oMNDNkM4WC@rabbit:5672/taiga'
result_backend = 'redis://anything:5mmGAxk8Eo@redis:6379/0'

accept_content = ['pickle',] # Values are 'pickle', 'json', 'msgpack' and 'yaml'
task_serializer = "pickle"
result_serializer = "pickle"

timezone = 'Europe/Moscow'

task_default_queue = 'tasks'
task_queues = (
    Queue('tasks', routing_key='task.#'),
    Queue('transient', routing_key='transient.#', delivery_mode=1)
)
task_default_exchange = 'tasks'
task_default_exchange_type = 'topic'
task_default_routing_key = 'task.default'
