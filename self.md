```shell
docker pull rabbitmq
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:latest
```
Access the RabbitMQ Management Dashboard
Open your web browser and navigate to http://localhost:15672/. Log in with the default credentials (guest/guest). Voila! You're now in the RabbitMQ Management Dashboard.