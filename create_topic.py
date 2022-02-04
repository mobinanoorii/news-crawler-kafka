from kafka.admin import KafkaAdminClient, NewTopic


admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:29092", 
    client_id='test'
)

topic_list = []
topic_list.append(NewTopic(name="news_topic_detection", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)
