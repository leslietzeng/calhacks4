from google.cloud import vision
from google.cloud.vision import types

import logger
import gcp_credentials


def send_image(content):
    """
        content = a Base64 encoded image string
    """


    # For internal debugging.

    # # The name of the image file to annotate
    # file_name = 'test.jpg'
    #
    # #Loads the image into memory
    # with io.open(file_name, 'rb') as image_file:
    #     content = image_file.read()


    image = types.Image(content=content)

    # Performs label detection on the image file

    response = client.label_detection(image=image)
    labels = response.label_annotations

    logger.log('Labels:')
    for label in labels:
        logger.log(label.description)

    return


def _get_client():
    creds = gcp_credentials.get_credentials()
    client = vision.ImageAnnotatorClient(credentials=creds)
    return client


# Instantiates a client
client = _get_client()