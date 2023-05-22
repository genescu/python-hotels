# Import the required modules
import requests
from bs4 import BeautifulSoup
import json
import re
from hotels.main.service import functions as fn
from hotels.main.entities import room, hotel


# Function will return a list of dictionaries
# each containing information of hotels.
def dictionary_bookingcom(soup):
    result = []
    node = soup.find('div', attrs={'id': 'hotelTmpl'})

    entity_model = hotel.Hotel()
    entity_model.set_name(node.find('span', attrs={'id': 'hp_hotel_name'}))
    entity_model.set_address(node.find('span', attrs={'id': 'hp_address_subtitle'}))

    classification = node.find('i', attrs={'class': re.compile('^ratings_stars_')})
    if classification is not None:
        classification = classification.get('class')
        for c in classification:
            if c.startswith('ratings_stars_'):
                classification = int(c.split('ratings_stars_')[1])
                if classification > 0:
                    entity_model.set_classification(classification)

    # description section
    # description contain multiple paragraphs

    description = ''
    property_description_content = node.find('div',
                                             attrs={'class': re.compile('^hotel_description_wrapper_exp')})
    if property_description_content is not None:
        description_p = []
        property_description_content = property_description_content.find_all('p')
        for p in property_description_content:
            description_p.append(p.get_text())
        description = " ".join(description_p)

    entity_model.set_description(description)
    # end description section

    # reviews_points

    reviews_points = node.find('span', attrs={'class': re.compile('^js--hp-scorecard-scoreval')})
    reviews_points = fn.parser(reviews_points)
    entity_model.set_reviews_points(reviews_points)

    # end reviews_points

    # reviews_number
    reviews_number = node.find('span', attrs={'class': re.compile('^score_from_number_of_reviews')})
    reviews_number = reviews_number.find('strong')
    reviews_number = fn.parser(reviews_number)
    entity_model.set_reviews_number(reviews_number)

    # end reviews_number

    room_type_area = node.find('table', attrs={'id': 'maxotel_rooms'})
    if room_type_area is not None:

        room_type_table = room_type_area.find_all('tr')
        if room_type_table is not None:
            for tr in room_type_table:
                room_categories = room.Room()

                # starting occupancy_max adults
                occupancy_max = tr.find('i', attrs={'class': re.compile('^occupancy_max')})
                if occupancy_max is not None:
                    room_type_max = occupancy_max.get('title')
                    if room_type_max is not None:
                        room_type_max = int(room_type_max.split(':')[1])
                        room_categories.set_adults(room_type_max)

                # starting room type
                room_type = tr.find('td', attrs={'class': re.compile('ftd')})
                room_categories.set_room_type(room_type)

                # check for kids
                plus_kids = tr.find('span', attrs={'class': re.compile('jq_tooltip with_kids')})
                if plus_kids is not None:
                    plus_kids_title = plus_kids.get('title')
                    if plus_kids_title is not None:
                        plus_kids_title = plus_kids_title.split('children')[1].split('(')[0]
                        kids = re.sub("[^0-9]", "", plus_kids_title)
                        room_categories.set_kids(kids)

                if room_categories.get_adults() > 0:
                    entity_model.room_categories.append(room_categories.get_props())

    # find alternative hotels
    alternative_hotels = []
    alternative_hotels_area = node.find('table', attrs={'id': 'althotelsTable'})
    if alternative_hotels_area is not None:
        alternative_hotels_area_row = alternative_hotels_area.find_all('td')
        if alternative_hotels_area_row is not None:
            for tr in alternative_hotels_area_row:
                alt_hotel = hotel.Hotel()
                alt_hotel.set_name(tr.find('a', attrs={'class': re.compile('^althotel_link')}))
                if alt_hotel.get_name():
                    #  start classification
                    classification = tr.find('i', attrs={'class': re.compile('^ratings_stars_')})
                    if classification is not None:
                        classification = classification.get('title')
                        classification = int(classification.split('-star')[0])
                        if classification > 0:
                            entity_model.set_classification(classification)
                        alt_hotel.set_classification(classification)

                    reviews_number = tr.find('span', attrs={'class': re.compile('^score_from_number_of_reviews')})
                    if reviews_number is not None:
                        reviews_number = reviews_number.find('strong')
                        alt_hotel.set_reviews_number(reviews_number)

                    reviews_points = tr.find('span', attrs={'class': re.compile('^rating')})

                    if reviews_points is not None:
                        reviews_points = reviews_points.find('span')
                        alt_hotel.set_reviews_points(reviews_points)

                    alt_hotel.set_description(tr.find('span', attrs={'class': re.compile('^hp_compset_description')}))
                    alternative_hotels.append(alt_hotel.get_props())

    # saving alternative hotels
    entity_model.set_alternative_hotels(alternative_hotels)

    result.append(entity_model.get_props())
    return result


def environment(env):
    if env == 'live':
        base_url = 'https://hotels.toscrape.com/catalogue/page-1.html'
        # requests.get(url) returns a response that is saved
        # in a response object called page.
        page = requests.get(base_url)
        soup = BeautifulSoup(page.text, 'html.parser')

    else:

        base_url = "../fixture/bristol.html"
        page = open(base_url)
        soup = BeautifulSoup(page, 'html.parser')

    print('Running ' + env)
    return soup


# Main Function
if __name__ == '__main__':
    # Enter the url of website

    env = 'dev'

    soup = environment(env)
    # Function will return a list of dictionaries
    res = dictionary_bookingcom(soup)

    with open('../output/hotels.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, indent=2, ensure_ascii=False)
    print('saved json file')
