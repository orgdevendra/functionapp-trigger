<<<<<<< HEAD
import logging
import azure.functions as func
from azure.messaging.webpubsubservice import WebPubSubServiceClient

def main(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus topic trigger function processed a message: %s', msg.get_body().decode('utf-8'))

    # Initialize Web PubSub client
    webpubsub_client = WebPubSubServiceClient.from_connection_string("WEBPUBSUB_CONNECTION_STR")

    # Send message to Web PubSub
    message = msg.get_body().decode('utf-8')
    webpubsub_client.send_to_all(message)
=======
import azure.functions as func
import logging

app = func.FunctionApp()

@app.service_bus_topic_trigger(arg_name="azservicebus", subscription_name="wind_topic", topic_name="wind_topic",
                               connection="servicebustopic0318_SERVICEBUS") 
def servicebus_topic_trigger(azservicebus: func.ServiceBusMessage):
    logging.info('Python ServiceBus Topic trigger processed a message: %s',
                azservicebus.get_body().decode('utf-8'))
>>>>>>> c584775 (initial functionapp commit)
