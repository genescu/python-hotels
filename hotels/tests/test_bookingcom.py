import unittest

from bs4 import BeautifulSoup

from hotels.main.bookingcom import dictionary_bookingcom


class TestBookingcom(unittest.TestCase):

    # 1. Test that the function returns a list of dictionaries:
    def test_dictionary_bookingcom(self):
        soup = BeautifulSoup(
            '<div id="hotel T mpl"><span id="hp_hot el_name"> Hotel Name<span id="hp_address_subtitle"> Address',
            "html.parser",
        )
        result = dictionary_bookingcom(soup)
        assert isinstance(result, list)
        assert all(isinstance(d, dict) for d in result)

    # 2. Test that the function sets the hotel name and address correctly:
    def test_dictionary_bookingcom_hotel_info(self):
        soup = BeautifulSoup(
            '<div id="hotel T mpl"><span id="hp_hot el_name"> Hotel Name<span id="hp_address_subtitle"> Address',
            "html.parser",
        )
        result = dictionary_bookingcom(soup)
        assert result[0]["name"] == "Hotel Name"
        assert result[0]["address"] == "Address"

    # 3. Test that the function sets the hotel classification correctly:
    def test_dictionary_bookingcom_classification(self):
        soup = BeautifulSoup(
            '<div id="hotel T mpl"><i class="ratings_st ars_4">', "html.parser"
        )
        result = dictionary_bookingcom(soup)
        assert result[0]["classification"] == 4

    # 4. Test that the function sets the hotel description correctly:
    def test_dictionary_bookingcom_description(self):
        soup = BeautifulSoup(
            '<div id="hotel T mpl"><div class="hotel_description_wrapper_exp"><p>This is the description.<p> It '
            "has multiple paragraphs.",
            "html.parser",
        )
        result = dictionary_bookingcom(soup)
        assert (
            result[0]["description"]
            == "This is the description. It has multiple paragraphs."
        )

    # 5. Test that the function sets the hotel reviews points and number correctly:
    def test_dictionary_bookingcom_reviews(self):
        soup = BeautifulSoup(
            '<div id="hotel T mpl"><span class="js-- hp-score card-score val">8.9<span '
            'class="score_from_number_of_reviews"><strong>1234 reviews',
            "html.parser",
        )
        result = dictionary_bookingcom(soup)
        assert result[0]["reviews_points"] == 8.9
        assert result[0]["reviews_number"] == 1234


if __name__ == "__main__":
    unittest.main()
