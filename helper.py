from api import ApiClient


def add_order(token):
    client = ApiClient()
    return client.create_order(token)


