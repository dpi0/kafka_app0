import json
from time import sleep
from faker import Faker

from kafka import KafkaProducer

fake = Faker()
producer = KafkaProducer(bootstrap_servers="localhost:29092")

TOPIC0 = "topic0"
WAITING_TIME: int = 10
DATA_LIMIT = 20


def data_generator():
    for unique_id in range(1, DATA_LIMIT + 1):
        data = {
            "id": unique_id,
            "name": f"{fake.name()}",
            "address": f"{fake.address()}",
        }
        yield data


print("Starting Producer...")
print(f"Sending a MSG every {WAITING_TIME} seconds")


def produce():
    for data in data_generator():
        data_json = json.dumps(data).encode("utf-8")
        producer.send(
            TOPIC0,
            data_json,
        )
        print("Sent! \n", data)
        sleep(WAITING_TIME)


if __name__ == "__main__":
    produce()
