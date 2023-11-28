import pika

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the 'hello' queue
channel.queue_declare(queue='hello')

# Define a callback function to handle incoming messages
def callback(ch, method, properties, body):
    print(" [x] Received:", body)

# Set up a consumer that calls the callback function for each message
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()