import os

from kafka import KafkaProducer

host=os.getenv("cust_host", "localhost")
port=os.getenv("cust_port", "29092")
topic=os.getenv("cust_topic", "test")

url = f"{host}:{port}"

if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers=url)
    while True:
        textToSend = input("Any thing to send out: ")
        textBin = textToSend.encode("utf-8")
        resultFut = producer.send(topic, textBin, b"python-msg")
        result = resultFut.get(timeout=60)
        print(result)