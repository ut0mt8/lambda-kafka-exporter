from chalice import Chalice, Response, Rate
from json import dumps
from kafka import KafkaProducer
import os

app = Chalice(app_name='kafka-gw')

@app.route('/event', methods=['POST'], content_types=['application/json'])
def post_event():
    kafka_servers = os.environ['KAFKA_SERVERS']
    kafka_topic = os.environ['KAFKA_TOPIC']
    data = app.current_request.json_body

    try:
        producer = KafkaProducer(bootstrap_servers=kafka_servers, value_serializer=lambda x: dumps(x).encode('utf-8'))
        producer.send(kafka_topic, value=data).get(timeout=10)
        return "yummy" 
    except e:
        return "blurp"
