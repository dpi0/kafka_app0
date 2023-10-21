from kafka import KafkaConsumer

TOPIC_ORDER_CREATED = "order_confirmed"

consumer = KafkaConsumer(
    TOPIC_ORDER_CREATED, bootstrap_servers="localhost:29092"
)

print("Starting Notify Consumer...")


def consume():
    while True:
        for msg in consumer:
            print("\n\n New MSG received! ✅")
            # print(msg.value.decode())


if __name__ == "__main__":
    consume()
