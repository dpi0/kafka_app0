from kafka import KafkaConsumer

TOPIC0 = "topic0"

consumer = KafkaConsumer(TOPIC0, bootstrap_servers="localhost:29092")

print("Starting Consumer...")

while True:
    for msg in consumer:
        print("\n\n New MSG received!")
        print(msg)
