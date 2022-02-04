from kafka import KafkaProducer
from kafka.errors import KafkaError
from crawler import Crawler

import jdatetime

class Producer:

    def __init__(self, crawler):
        self.crawler = crawler
        self.producer = KafkaProducer(bootstrap_servers=['localhost:29092'], retries=5)

    def get_todat_date(self):
        x = jdatetime.datetime.now()
        return str(x.date()).replace('-', '/')

    def on_send_success(self, record_metadata):
        print(record_metadata.topic)
        print(record_metadata.partition)
        print(record_metadata.offset)

    def on_send_error(self, excp):
        print('I am an errback!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        # handle exception

    def produce_tabnak(self):
        date = self.get_todat_date()
        for word in crawler.tabnak_crawler_job(date, date):
            # produce asynchronously with callbacks
            self.producer.send('news_topic_detection', key=bytes(f'tabnak_{date}', 'utf-8'), value=bytes(word, 'utf-8')).add_callback(self.on_send_success).add_errback(
                self.on_send_error)

        # block until all async messages are sent
        self.producer.flush()

    def produce_yjc(self):
        date = self.get_todat_date()
        for word in crawler.yjc_crawler_job(date, date):
            # produce asynchronously with callbacks
            self.producer.send('news_topic_detection', key=bytes(f'yjc_{date}', 'utf-8'), value=bytes(word, 'utf-8')).add_callback(self.on_send_success).add_errback(
                self.on_send_error)

        # block until all async messages are sent
        self.producer.flush()

crawler = Crawler()
producer = Producer(crawler)
producer.produce_tabnak()
producer.produce_yjc()
