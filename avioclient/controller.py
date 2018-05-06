# -*- coding: utf-8 -*-
from avioclient.send_data import SendControls
from avioclient import config
from datetime import datetime

MAX_POSITION = 600
MIN_POSITION = 200


def send_data_test():
    """
    simple test method
    """
    data_sender = SendControls(config.SERVER_URL)
    connections_done = 0
    position = MIN_POSITION
    direction = 1
    step = 50
    while True:
        connections_done += 1
        print(
            data_sender.get_data(
                config.GET_ENDPOINT.format(
                    connection_id=connections_done
                )
            )
        )
        print(datetime.utcnow())
        # check duration of call
        print(
            data_sender.post_data(
                config.POST_ENDPOINT.format(
                    connection_id=connections_done
                ),
                data={
                    "position": position
                }
            )
        )
        print(datetime.utcnow())
        if connections_done > (MAX_POSITION/step)+1:
            break

        if direction == 1:
            position = position+step
        else:
            position = position-step

        if position <= MIN_POSITION or position >= MAX_POSITION:
            position = MIN_POSITION if position <= MIN_POSITION else MAX_POSITION
            direction = 0 if direction else 1


if __name__ == "__main__":
    send_data_test()
