from kafka import KafkaConsumer

TOPIC_ORDER_CREATED = "order_confirmed"

consumer = KafkaConsumer(
    TOPIC_ORDER_CREATED, bootstrap_servers="localhost:29092"
)

print("Starting Analytics Consumer...")


def consume():
    TOTAL_ORDERS_RECVD = 0

    while True:
        for msg in consumer:
            print("\n\n New MSG received! ✅")
            print("Analysing Data...🔃")
            # print(msg.value.decode())
            TOTAL_ORDERS_RECVD += 1
            print("Total orders received today:", TOTAL_ORDERS_RECVD)


if __name__ == "__main__":
    consume()
