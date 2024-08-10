from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Setup Selenium WebDriver
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

def get_places(driver, lat, lng, radius_km, category, subcategory):
  places = []
  search_query = f'{subcategory} {category}'
  url = f'https://www.google.com/maps/search/{search_query}/@{lat},{lng},{radius_km}z'

  driver.get(url)

  page_content = driver.page_source
  soup = BeautifulSoup(page_content, "html.parser")
  data_elements = soup.find_all("div", class_="Nv2PK")
  for element in data_elements[:10]:
    try:
      name = element.select_one('.qBF1Pd').text.strip() if element.select_one('.qBF1Pd') else ''
      rating = element.select_one('.MW4etd').text.strip() if element.select_one('.MW4etd') else ''
      link = element.select_one('a').get('href') if element.select_one('a') else ''

      places.append({
        'name': name,
        'address': '',
        'phone_number': '',
        'rating': rating,
        'link': link
      })
    except Exception as e:
      continue
  
  return places

def get_reviews(driver, place):
  reviews = []

  driver.get(place['link'])

  page_content = driver.page_source
  soup = BeautifulSoup(page_content, "html.parser")

  # Get address and phone number
  address_element = soup.find("button", class_="CsEnBe", attrs={"data-item-id": "address"})
  phone_number_element = soup.find("button", class_="CsEnBe", attrs={"data-tooltip":"Copy phone number"})
  if address_element:
      place['address'] = address_element.get('aria-label') if address_element.get('aria-label') else ''
  if phone_number_element:
      place['phone_number'] = phone_number_element.get('aria-label') if phone_number_element.get('aria-label') else ''

  # Click on the "Reviews" tab
  reviews_tab_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label*='Reviews for']")
  reviews_tab_button.click()

  retry = 0
  while True:
    # retry till reviews element found
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, "html.parser")
    review_divs = soup.find_all("div", class_="jftiEf")
    if len(review_divs) > 0:
      break
    time.sleep(0.5)

    retry += 1
    if retry>20:
      break

  for review_div in review_divs:
    try:
      author = review_div.find('div', class_='d4r55').text.strip()
      date = review_div.find('span', class_='rsqaWe').text.strip()
      text = review_div.find('span', class_='wiI7pd').text.strip()
      
      reviews.append({
        'author': author,
        'date': date,
        'text': text
      })
    except Exception as e:
      continue

  return place, reviews

if __name__ == "__main__":
  latitude = 30.7046
  longitude = 76.7179
  radius_km = 10
  category = 'Restaurant'
  subcategory = 'Vegetarian'

  driver = webdriver.Chrome(options=options)

  places = get_places(driver, latitude, longitude, radius_km, category, subcategory)
  for place in places:
    place, reviews = get_reviews(driver, place) 
    print("\n")
    print(f"Name: {place['name']}")
    print(f"Rating: {place['rating']}")
    print(f"Phone Number: {place['phone_number']}")
    print(f"Address: {place['address']}")
    print(f"URL: {place['link']}")
    print("Reviews:")
    for review in reviews:
      print(f" - {review}")
    print("\n")

  driver.quit()
