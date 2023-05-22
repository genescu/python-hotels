import unittest
from hotels.main.validators.hotelvalidator import Validate
from hotels.main.service.functions import parser
from hotels.main.entities.hotel import Hotel

class TestHotel(unittest.TestCase):

    def setUp(self):
        self.hotel = Hotel()

    def test_set_name(self):
        self.hotel.set_name('Hilton')
        self.assertEqual(self.hotel.get_name(), 'Hilton')

    def test_set_address(self):
        self.hotel.set_address('123 Main St.')
        self.assertEqual(self.hotel.get_address(), '123 Main St.')

    def test_set_classification(self):
        self.hotel.set_classification(4)
        self.assertEqual(self.hotel.get_classification(), 4)

    def test_set_reviews_points(self):
        self.hotel.set_reviews_points(8.345)
        self.assertEqual(self.hotel.get_reviews_points(), 8.35)

    def test_set_reviews_number(self):
        self.hotel.set_reviews_number(1001)
        self.assertEqual(self.hotel.get_reviews_number(), 1001)

    def test_set_description(self):
        self.hotel.set_description('A luxurious hotel in the heart of the city')
        self.assertEqual(self.hotel.get_description(), 'A luxurious hotel in the heart of the city')

    def test_set_room_categories(self):
        self.hotel.set_room_categories(['Single', 'Double', 'Suite'])
        self.assertListEqual(self.hotel.get_room_categories(), ['Single', 'Double', 'Suite'])

    def test_set_alternative_hotels(self):
        self.hotel.set_alternative_hotels(['Marriott', 'Sheraton', 'Hyatt'])
        self.assertListEqual(self.hotel.get_alternative_hotels(), ['Marriott', 'Sheraton', 'Hyatt'])

    def test_get_props(self):
        self.hotel.set_name('Hilton')
        self.hotel.set_address('123 Main St.')
        self.hotel.set_classification(4)
        self.hotel.set_reviews_points(8.345)
        self.hotel.set_reviews_number(1001)
        self.hotel.set_description('A luxurious hotel in the heart of the city')
        self.hotel.set_room_categories(['Single', 'Double', 'Suite'])
        self.hotel.set_alternative_hotels(['Marriott', 'Sheraton', 'Hyatt'])
        props = self.hotel.get_props()
        self.assertIsInstance(props, dict)
        Validate(**props)


