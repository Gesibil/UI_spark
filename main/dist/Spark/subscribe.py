import paho.mqtt.client as mqtt

# MQTT broker information
mqtt_broker = "mqtt-dashboard.com"  # Replace with the Mosquitto broker address
mqtt_port = 8884  # Default MQTT port
mqtt_topic = "face_detection/alert"

# Callback function for when a message is received
def on_message(client, userdata, message):
    print("Received message:", message.payload.decode())

# Create MQTT client instance
client = mqtt.Client()

# Set callback function
client.on_message = on_message

# Connect to the MQTT broker
client.connect(mqtt_broker, mqtt_port)

# Subscribe to the topic
client.subscribe(mqtt_topic)

# Start the MQTT client loop to receive messages
client.loop_start()

# Keep the script running to continue receiving messages
while True:
    pass

# Disconnect from the MQTT broker
client.disconnect()
