from time import sleep
from faker import Faker
from json import dumps


from kafka import KafkaProducer

fake = Faker()
producer = KafkaProducer(bootstrap_servers="localhost:29092")

TOPIC_ORDER_CREATED = "order_created"
WAITING_TIME: int = 10
DATA_LIMIT = 20


def data_generator():
    for unique_id in range(1, DATA_LIMIT + 1):
        data = {
            "user_id": unique_id,
            "name": f"{fake.name()}",
            "address": f"{fake.address()}",
            "order_name": f"{fake.text()}",
        }
        yield data


print("Starting Producer...")
print(f"Sending a MSG every {WAITING_TIME} seconds")


def produce():
    for data in data_generator():
        data_json = dumps(data).encode("utf-8")
        producer.send(
            TOPIC_ORDER_CREATED,
            data_json,
        )
        print("Sent! \n", data)
        sleep(WAITING_TIME)


if __name__ == "__main__":
    produce()
