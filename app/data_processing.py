from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import dumps, loads
from uuid import uuid4

TOPIC_ORDER_CREATED = "order_created"
TOPIC_ORDER_CONFIRMED = "order_confirmed"

processing_producer = KafkaProducer(bootstrap_servers="localhost:29092")
processing_consumer = KafkaConsumer(
    TOPIC_ORDER_CREATED, bootstrap_servers="localhost:29092"
)

print("Staring Data Processing Consumer...")


def producer(data):
    data_json = dumps(data).encode("utf-8")
    processing_producer.send(TOPIC_ORDER_CONFIRMED, data_json)

    print("Data Sent to the Pipeline 🪈 \n\n")


def consumer():
    while True:
        for msg in processing_consumer:
            print("Received new MSG! ✅")
            print("Starting Processing 🔃...")

            msg_json = loads(msg.value.decode())

            order_confirmed_id = uuid4()
            order_name = msg_json["order_name"]
            user_id = msg_json["user_id"]
            user_name = msg_json["name"]
            address = msg_json["address"]

            data = {
                "order_id": f"{order_confirmed_id}",
                "order_name": order_name,
                "customer_id": user_id,
                "customer_name": user_name,
                "customer_address": address,
            }

            print(data)
            print("Processing Completed! ✅")

            producer(data)


if __name__ == "__main__":
    consumer()
