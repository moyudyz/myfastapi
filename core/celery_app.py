from celery import Celery

# celery_app = Celery(
#     "worker", broker="amqp://moyu:moyu2020@localhost:5672/moyu")

celery_app = Celery(
    "worker", broker="redis://@127.0.0.1:6379/1")

celery_app.conf.task_routes = {"worker.test_celery": "main-queue"}
