from kafka import KafkaConsumer
from mapreduce import TopicMapReduce


# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('news_topic_detection',
                            group_id='my-group',
                            auto_offset_reset='earliest', enable_auto_commit=True,
                            bootstrap_servers=['localhost:29092'], consumer_timeout_ms=9000)
mapreduce = TopicMapReduce()

for message in consumer:
    mapreduce.map(message.value.decode('utf-8'))

for x in mapreduce.reduce():
    print(x)

