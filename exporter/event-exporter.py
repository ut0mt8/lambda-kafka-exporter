from json import loads
from kafka import KafkaConsumer
from prometheus_client import start_http_server, Counter

topic = 'XXX'
group = 'XXX'

EVENT_COUNT = Counter('event_count', 'Number of events processed', ['group'])
EVENT_DURATION = Counter('event_duration', 'Duration of events processed', ['group'])

consumer = KafkaConsumer(topic,
    bootstrap_servers=['127.0.0.1:9092'],
    enable_auto_commit=True,
    group_id=group,
    value_deserializer=lambda x: loads(x.decode('utf-8')))

start_http_server(8000)
for msg in consumer:
    data = msg.value
    print data
    if 'group' not in data:
        print "malformed event, missing group field"
    elif 'duration' not in data:
        print "malformed event, missing duration field"
    else:
        if type(data['duration']) is not int:
            print "duration field is not an integer"
        else:
            EVENT_COUNT.labels(data['group']).inc()
            EVENT_DURATION.labels(data['group']).inc(data['duration'])
            print "ok"

