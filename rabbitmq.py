import pika

class RabbitMQConnection:
    def __init__(self, host: str, queue_name: str):
        self.connection: pika.BlockingConnection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel: pika.adapters.blocking_connection.BlockingChannel = self.connection.channel()
        self.queue_name: str = queue_name

    def send_message(self, message: str):
        self.channel.queue_declare(queue=self.queue_name)
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=message)

    def close_connection(self):
        self.connection.close()

if __name__ == "__main__":
    # Usage example
    connection = RabbitMQConnection("localhost", "image_queue")

    # Send a message to RabbitMQ
    connection.send_message("Message to RabbitMQ")

    # Close the RabbitMQ connection
    connection.close_connection()
