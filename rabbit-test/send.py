import pika

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue named 'hello'
channel.queue_declare(queue='hello')

# Publish a message to the 'hello' queue
message = "Hello, RabbitMQ!"
channel.basic_publish(exchange='', routing_key='hello', body=message)

print(" [x] Sent:", message)

# Close the connection
connection.close()