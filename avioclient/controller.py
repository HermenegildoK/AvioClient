# -*- coding: utf-8 -*-
from avioclient.send_data import SendControls
from avioclient import config


def send_data():
    data_sender = SendControls(config.SERVER_URL)
    connections_done = 0
    while True:
        connections_done += 1
        print(
            data_sender.get_data(
                config.GET_ENDPOINT.format(
                    connection_id=connections_done
                )
            )
        )
        print(
            data_sender.post_data(
                config.POST_ENDPOINT.format(
                    connection_id=connections_done
                ),
                data={
                    "position": "LEFT",
                    "offset": 180
                }
            )
        )
        if connections_done > 100:
            break


if __name__ == "__main__":
    send_data()
