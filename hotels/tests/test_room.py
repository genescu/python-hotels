import unittest
from hotels.main.validators.hotelvalidator import Validate
from hotels.main.service.functions import parser
from hotels.main.entities.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room()

    def test_set_adults(self):
        self.room.set_adults('2')
        self.assertEqual(self.room.get_adults(), 2)

    def test_set_kids(self):
        self.room.set_kids('1')
        self.assertEqual(self.room.get_kids(), 1)

    def test_set_room_type(self):
        self.room.set_room_type('single')
        self.assertEqual(self.room.get_room_type(), 'single')

    def test_invalid_adults(self):
        self.room.set_adults('-1')
        self.assertEqual(self.room.get_adults(), 0)

    def test_invalid_kids(self):
        self.room.set_kids('-1')
        self.assertEqual(self.room.get_kids(), 0)

    def test_validate_room(self):
        self.room.set_adults('2')
        self.room.set_kids('1')
        self.room.set_room_type('single')
        self.assertEqual(self.room.get_props(), {'adults': 2, 'kids': 1, 'room_type': 'single'})


if __name__ == '__main__':
    unittest.main()
