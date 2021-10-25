from time import sleep
from json import dumps
from kafka import KafkaProducer
import random

cities = ["Ростов", "Москва", "Батайск", "Питер", "Воронеж", "ИИС"]
events = ["Убийство", "Строительсто", "Уборка", "Выборы", "Субботник", "Футбол"]

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(10): 
    random_cities = random.randint(0, len(cities) - 1)
    random_events = random.randint(0, len(events) - 1)
    #data = {cities[random_cities] : events[random_events]}
    data = {"city": cities[random_cities], "event": events[random_events]}
    print(data)
    producer.send('cities_events', value=data)
    sleep(1)

    