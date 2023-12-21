from django.test import TestCase

class Astronaut:
    def __init__(self):
        pass

    def launch_mission(self) -> bool:
        mission_successful = False
        spacecraft_ready = True

        if spacecraft_ready:
            mission_successful = True

        return mission_successful

    def send_message_to_earth(self) -> str:
        return "Message from space: All systems go!"

class TestAstronaut(TestCase):
    def test_launch_mission(self):
        astronaut = Astronaut()
        self.assertTrue(astronaut.launch_mission())


