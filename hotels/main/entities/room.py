import hotels.main.validators.roomvalidator as validate
import hotels.main.service.functions as fn


class Room:
    def __init__(self):
        self.adults = 0
        self.kids = 0
        self.room_type = ''

    def get_adults(self):
        return self.adults

        # setter method

    def set_adults(self, x):
        if x is not None:
            x = int(fn.parser(x))
            if x > 0:
                self.adults = x

    def get_kids(self):
        return self.kids

    # setter method

    def set_kids(self, x):
        x = int(fn.parser(x))
        if x > 0:
            self.kids = x

    def get_room_type(self):
        return self.room_type

    # setter method

    def set_room_type(self, x):
        if x is not None:
            self.room_type = fn.parser(x)

    def get_props(self):
        data: Room = {
            'adults': self.get_adults(),
            'kids': self.get_kids(),
            'room_type': self.get_room_type(),
        }
        validate.Validate(**data)
        return vars(self)
