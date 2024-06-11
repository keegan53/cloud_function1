def process_iot_data(event, context):
    """Cloud Function to process incoming IoT data from Pub/Sub.
    Args:
        event (dict): The event payload.
        context (google.cloud.functions.Context): The context object.
    """
    # Extracting data from the Pub/Sub message
    data = event['data']
    attributes = event['attributes']

    # Process the IoT data
    # Example: Print the data and attributes
    print(f"IoT Data: {data}")
    print(f"Attributes: {attributes}")

    # Perform further data processing or storage operations
    # Example: Store the data in a database or send it to another system
