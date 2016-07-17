"""
Python module that connects to MQTT broker and subscribes to topic.
Data is received and persisted to local Postgres database.
"""
import paho.mqtt.client as mqtt

import db

# ----- Global config variables -----
MQTT_HOST = 'mosquitto'
MQTT_PORT = 1883
MQTT_TOPIC = 'pygotham'
MQTT_CLIENT_ID = 'data_collector'
MQTT_USERNAME = ''
MQTT_PASSWORD = ''

# The callback function for when the client connects to broker
def on_connect(client, userdata, rc):
    """
    Callback function used to connect to the Mosquitto message broker.
    """
    print('Connected with result code ' + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC, 1)
    

def on_message(client, userdata, msg):
    """
    Callback function for when new sensor data is received.
    """
    print('New message: {}'.format(msg.payload))
    # Decode message to string
    msg = msg.payload.decode("utf-8")
    db.write_record(msg)
    
    
if __name__ == '__main__':

    # Create an MQTT client instance and authenticate
    client = mqtt.Client(client_id=MQTT_CLIENT_ID)
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

    # Register callback functions
    client.on_connect = on_connect    
    client.on_message = on_message

    # This is where the MQTT service connects and starts listening for messages
    client.connect(MQTT_HOST, MQTT_PORT, 60)

    # Blocking call to wait for messages
    client.loop_forever()
