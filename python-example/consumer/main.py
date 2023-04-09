import os

from kafka import KafkaConsumer

host=os.getenv("cust_host", "localhost")
port=os.getenv("cust_port", "29092")

url = f"{host}:{port}"


if __name__ == '__main__':
    consumer = KafkaConsumer(bootstrap_servers=url)
    consumer.subscribe("test")
    for msg in consumer:
        print(msg)
