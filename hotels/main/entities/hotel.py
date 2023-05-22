import hotels.main.validators.hotelvalidator as hotelvalidator
import hotels.main.service.functions as fn


class Hotel:
    def __init__(self):
        self.name = None
        self.address = None
        self.classification = None
        self.reviews_points = None
        self.reviews_number = None
        self.description = None
        self.room_categories = []
        self.alternative_hotels = []

    def get_name(self) -> str:
        return self.name

        # setter method

    def set_name(self, x):
        x = fn.parser(x, 'str')
        if x is not None:
            self.name = x

    def get_address(self) -> str:
        return self.address

    # setter method

    def set_address(self, x):
        x = fn.parser(x, 'str')
        if x is not None:
            self.address = x

    def get_classification(self) -> int:
        return self.classification

    # setter method

    def set_classification(self, x):
        x = fn.parser(x, 'int')
        if x is not None:
            x = int(x)
            if x > 0:
                self.classification = x
    def get_reviews_points(self) -> float:
        return self.reviews_points

    # setter method

    def set_reviews_points(self, x):
        x = fn.parser(x, 'float')
        if x is not None:
            self.reviews_points = float("{:.2f}".format(float(x)))

    def get_reviews_number(self) -> int:
        return self.reviews_number

    # setter method

    def set_reviews_number(self, x):
        x = fn.parser(x, 'int')
        if x is not None:
            x = int(x)
            if x > 0:
                self.reviews_number = x

    def get_description(self) -> str:
        return self.description

    # setter method

    def set_description(self, x):
        x = fn.parser(x, 'str')
        if x is not None:
            self.description = x

    def get_room_categories(self):
        return self.room_categories

    # setter method

    def set_room_categories(self, x):
        if x is not None:
            self.room_categories = x

    def get_alternative_hotels(self):
        return self.alternative_hotels

    # setter method

    def set_alternative_hotels(self, x):
        if x is not None:
            self.alternative_hotels = x

    def get_props(self):
        data: Hotel = {
            'name': self.get_name(),
            'address': self.get_address(),
            'classification': self.get_classification(),
            'reviews_points': self.get_reviews_points(),
            'reviews_number': self.get_reviews_number(),
            'description': self.get_description(),
            'room_categories': self.get_room_categories(),
            'alternative_hotels': self.get_alternative_hotels(),
        }
        hotelvalidator.Validate(**data)
        return vars(self)
