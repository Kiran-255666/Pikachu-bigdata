from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Set up producer configuration
producer_conf = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker(s)
    'client.id': 'python-producer'
}

# Create Kafka producer
producer = Producer(producer_conf)

# Send a sample message to a topic
topic = 'test-topic'
key = 'key1'
value = 'Hello, Kafka!'
producer.produce(topic, key=key, value=value, callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery reports received
producer.flush()
