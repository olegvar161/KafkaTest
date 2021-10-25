from kafka import KafkaConsumer
from json import loads
import pandas as pd

consumer = KafkaConsumer(
    'PAGEVIEWS_REGIONS',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='latest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message
    print(message)
    

