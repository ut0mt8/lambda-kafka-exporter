Small POC of a pattern sending event to a lambda and exposing it for scraping by prometheus.
The lambda is written with the chalice framework, and then send the event to a kafka topic.
The exporter consume event from the kafka topics and then present in the prometheus format.
Everything is written in python for simplicity purpose.

```
Event POST -> api-gw -> Lambda -> Kafka <- python consumer/exporter <- prometheus
```

Example payload:

```
{
	"group" : "evt1",
	"duration": 4500
}
```

Exported prometeus metrics:
```
# HELP event_count_total Number of events processed
# TYPE event_count_total counter
event_count_total{group="evt1"} 1.0
event_count_total{group="evt2"} 2.0
# HELP event_duration_total Duration of events processed
# TYPE event_duration_total counter
event_duration_total{group="evt1"} 4500.0
event_duration_total{group="evtg2"} 9130.0
```
