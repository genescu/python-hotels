# Python parser for booking.com

Steps to run: 

Firstly, you need to import the project.

Next, set the environment to either' dev' or' live'.

After that, navigate to the main folder and run the file named '**bookingcom.py**'. Once done, you will find a '**hotels.json**' file generated in the output folder.

Additionally, the project also provides unit tests as a bonus feature.

**Description**:


A Python script that scrap hotel information from a website and saves it as a JSON file. 

It uses the requests and BeautifulSoup modules to make requests to the website and parse the HTML content, respectively. 

The dictionary_booking com function extracts information about hotels from the parsed HTML and creates instances of the hotel.Hotel class to store the information. 

The environment function determines whether to run the script in a live or development environment by specifying the URL of the website to scrape. 

Finally, the main function runs the scraping process and saves the resulting hotel information as a JSON file.

