import time
from azure.iot.device import IoTHubDeviceClient, Message
import base64
def send_email_with_attachment(frame):
    CONNECTION_STRING = "HostName=jetson-nano.azure-devices.net;DeviceId=lap;SharedAccessKey=CsIolHcKWVI5SGksZIa809o/gz4wd/hboAIoTFiZZbo="
    IMAGE_FILE_PATH = frame  # Path to your image file

    def iothub_client_init():
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        return client

    def send_image(client):
        while True:
            try:
                with open(IMAGE_FILE_PATH, "rb") as image_file:
                    image_data = image_file.read()
                    encoded_image = base64.b64encode(image_data)

                msg = Message(encoded_image)
                print("Sending image message...")
                client.send_message(msg)
                print("Image message successfully sent to Azure IoT Hub.")
                time.sleep(5)  # Send message every 5 seconds
            except Exception as e:
                print("Error sending image message:", e)
                time.sleep(10)

    if __name__ == "__main__":
        try:
            client = iothub_client_init()
            send_image(client)
        except KeyboardInterrupt:
            print("IoT Hub client stopped")

