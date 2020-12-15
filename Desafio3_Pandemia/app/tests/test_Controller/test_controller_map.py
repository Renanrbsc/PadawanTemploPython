from unittest import TestCase
from app.Model.model_map import Map
from app.Controller.controller_map import CtrlMap


class TestMap(TestCase):

    def test_init(self):
        # Arrange
        new_controller = CtrlMap()
        # Action
        object_of_class = new_controller._model
        # Assertion
        self.assertIsInstance(object_of_class, Map)
