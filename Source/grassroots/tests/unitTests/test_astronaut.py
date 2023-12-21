from django.test import TestCase


def launch_mission() -> bool:
    mission_successful = False
    spacecraft_ready = True

    if spacecraft_ready:
        mission_successful = True

    return mission_successful

