import configuration
import data
import requests


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body)


def get_track_number(track):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER_TRACK + str(track))


def track_number_order():
    track_number = post_new_order()
    return track_number.json()['track']
