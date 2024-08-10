# GoogleMapsScraper

**GoogleMapsScraper** is a Python-based tool designed to scrape location details and user reviews from Google Maps using **Selenium** and **BeautifulSoup**. This script allows you to gather data on nearby places, including their names, ratings, addresses, phone numbers, and reviews.

## Key Features

- **Place Data Scraping:** Extract names, ratings, addresses, and phone numbers of places from Google Maps based on a specific category and subcategory.
- **Review Scraping:** Collect user reviews, including author names, review dates, and review text.
- **Headless Browser:** Uses Selenium's headless mode for fast and efficient scraping.
- **BeautifulSoup Integration:** Parses and extracts HTML content efficiently using BeautifulSoup.

## Getting Started

### Installation

Follow these steps to set up the **GoogleMapsScraper** tool:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/GoogleMapsScraper.git
   cd GoogleMapsScraper
   
2. **Install dependencies:**

   Make sure you have Python 3.7+ installed, then install the required packages:
   ```bash
     pip install selenium beautifulsoup4

3. **Download WebDriver:**

   Download the appropriate Chrome WebDriver for your version of Chrome from ChromeDriver download.
   Ensure the WebDriver executable is in your system's PATH, or specify the path in the script.

## Usage
  Script Configuration
  - Latitude & Longitude: Set the latitude and longitude variables to define the center of your search area.
  - Radius: Adjust the radius_km variable to set the search radius in kilometers.
  - Category & Subcategory: Define the category and subcategory to specify the types of places you want to scrape.

## Example Usage
To scrape places and reviews in your desired location:

1. **Run the script:**

   ```bash
   python google_map_scraper.py

2. **Output:**
   
   The script will output the name, rating, phone number, address, and reviews for each place.
   Example output:
   ```bash
    Name: Vegetarian Restaurant XYZ
    Rating: 4.5
    Phone Number: +1-234-567-890
    Address: 123 Main St, Your City, Country
    URL: https://www.google.com/maps/place/...
    Reviews:
     - {'author': 'John Doe', 'date': '1 month ago', 'text': 'Great food!'}
     - {'author': 'Jane Smith', 'date': '2 weeks ago', 'text': 'Excellent service!'}

## Contributing
We welcome contributions to GoogleMapsScraper! Feel free to fork the repository, create a branch, and submit a Pull Request with your improvements or new features.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

  
