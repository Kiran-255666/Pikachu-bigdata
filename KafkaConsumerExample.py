from confluent_kafka import Consumer, KafkaError

# Set up consumer configuration
consumer_conf = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker(s)
    'group.id': 'test-group',
    'auto.offset.reset': 'earliest'
}

# Create Kafka consumer
consumer = Consumer(consumer_conf)

# Subscribe to a topic
topic = 'test-topic'
consumer.subscribe([topic])

# Poll for messages
while True:
    msg = consumer.poll(1.0)  # Adjust the timeout as needed
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break
    print('Received message: Key = {}, Value = {}'.format(msg.key(), msg.value()))

# Close the consumer
consumer.close()
