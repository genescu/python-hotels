from unittest import TestCase

from hotels.main.entities.hotel import Hotel


class TestHotel(TestCase):
    pass

    def test_valid_name(self):
        data = "Bristol"
        unit = Hotel()
        unit.set_name(data)
        self.assertEqual(unit.get_name(), "Bristol")

        data = "Bristol  "
        unit = Hotel()
        unit.set_name(data)
        self.assertEqual(unit.get_name(), "Bristol")

    def test_invalid_name(self):
        data = 123
        unit = Hotel()
        unit.set_name(data)
        self.assertEqual(unit.get_name(), None)

        data = None
        unit = Hotel()
        unit.set_name(data)
        self.assertEqual(unit.get_name(), None)

        data = []
        unit = Hotel()
        unit.set_name(data)
        self.assertEqual(unit.get_name(), None)

    def test_valid_reviews_points(self):
        data = 9.7
        unit = Hotel()
        unit.set_reviews_points(data)
        self.assertEqual(unit.get_reviews_points(), 9.7)

        data = 9
        unit = Hotel()
        unit.set_reviews_points(data)
        self.assertEqual(unit.get_reviews_points(), 9.00)

    def test_invalid_reviews_points(self):
        data = "  "
        unit = Hotel()
        unit.set_reviews_points(data)
        self.assertEqual(unit.get_reviews_points(), None)

        data = None
        unit = Hotel()
        unit.set_reviews_points(data)
        self.assertEqual(unit.get_reviews_points(), None)

        data = []
        unit = Hotel()
        unit.set_reviews_points(data)
        self.assertEqual(unit.get_reviews_points(), None)

    def test_valid_reviews_number(self):
        data = 22

        unit = Hotel()
        unit.set_reviews_number(data)
        self.assertEqual(unit.get_reviews_number(), 22)

    def test_invalid_reviews_number(self):
        data = "a"
        unit = Hotel()
        unit.set_reviews_number(data)
        self.assertEqual(unit.get_reviews_number(), None)

        data = None
        unit = Hotel()
        unit.set_reviews_number(data)
        self.assertEqual(unit.get_reviews_number(), None)

        data = []
        unit = Hotel()
        unit.set_reviews_number(data)
        self.assertEqual(unit.get_reviews_number(), None)
