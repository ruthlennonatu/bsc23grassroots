from django.test import TestCase


def launch_mission() -> bool:
    mission_successful = False
    spacecraft_ready = True

    if spacecraft_ready:
        mission_successful = True

    return mission_successful


def send_message_to_earth() -> str:
    return "Message from space: All systems go!"


class Astronaut:
    def __init__(self):
        pass

