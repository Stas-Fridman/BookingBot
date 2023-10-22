from hotels import const
from hotels import os, time, csv, re, webdriver, By, WebDriverWait, EC, Keys, ActionChains, Select, pd

class Hotels(webdriver.Chrome):
    def __init__(self, driver_path = r"C:\your-path-to-chrome-driver", teardown=False): 
        # Initialize the web driver with optional path and teardown
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Hotels, self).__init__(options=options)
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Define an exit method to close the browser
        if self.teardown:
            time.sleep(5)
            self.quit()

    def landFirstPage(self):
        # Navigate to the initial landing page
        self.get(const.BASE_URL)

    def cancelCommercial(self):
        # Cancel any commercial pop-ups
        for _ in range(2):
            element = self.find_element(By.CLASS_NAME, 'a83ed08757')
            # Check if the element exists
            if element:
                try:
                    element.click()
                except:
                    pass

    def destinationPlace(self):
        # Set the destination for your trip
        where_to = self.find_element(By.XPATH, '//input[@placeholder="Where are you going?"]')
        where_to.clear()
        where_to.send_keys(f"{const.DESTINATION}")
        where_to.send_keys(Keys.TAB)

    def changeCurrency(self):
        # Change the currency
        if const.CURRENCY == "EURO":
            money_button = self.find_element(By.XPATH, '//button[@data-testid="header-currency-picker-trigger"]').click()
            euro = self.find_element(By.XPATH, '//span[contains(.,"Euro")]').click()
        elif const.CURRENCY == "USD":
            money_button = self.find_element(By.XPATH, '//button[@data-testid="header-currency-picker-trigger"]').click()
            usd = self.find_element(By.XPATH, '//span[contains(.,"U.S. Dollar")]').click()
        elif const.CURRENCY == "ILS":
            money_button = self.find_element(By.XPATH, '//button[@data-testid="header-currency-picker-trigger"]').click()
            ils = self.find_element(By.XPATH, '//span[contains(.,"Israeli New Shekel")]').click()
        else:
            pass

    def tripDates(self):
        # Set the check-in and check-out dates
        check_in_year_month = self.find_element(By.XPATH, '//select[@data-name="year-month"]')
        select_check_in = Select(check_in_year_month)
        select_check_in.select_by_value(f"{const.CHECK_IN_YEAR}-{const.CHECK_IN_MONTH}")
        # check_in_year_month.send_keys("2023-12")

        check_in_day = self.find_element(By.XPATH , '//select[@data-name="day"]')
        select_check_day = Select(check_in_day)
        select_check_day.select_by_value(f"{const.CHECK_IN_DAY}")
        # check_in_day.send_keys("10")
        check_in_day.send_keys(Keys.TAB)

        check_out_year_month = self.find_element(By.XPATH, '//select[@data-name="year-month"]')
        select_check_out = Select(check_out_year_month)
        select_check_out.select_by_value(f"{const.CHECK_OUT_YEAR}-{const.CHECK_OUT_MONTH}")
        # check_out_year_month.send_keys("2023-12")

        check_out_day = self.find_element(By.XPATH , '//select[@data-name="day"]')
        select_check_out_day = Select(check_out_day)
        select_check_out_day.select_by_value(f"{const.CHECK_OUT_DAY}")
        # check_out_day.send_keys("30")
        check_out_day.send_keys(Keys.TAB)

    def numberOfTravelers(self):
        # Set the number of travelers, including adults, children, and rooms
        how_many_btn = self.find_element(By.XPATH, '//button[@class="a83ed08757 ebbedaf8ac ada2387af8"]').click()
        adults_children_rooms = self.find_elements(By.CLASS_NAME, 'd723d73d5f')
        num_of_adults = int(adults_children_rooms[0].text) # adults
        num_of_children = int(adults_children_rooms[1].text) # children
        num_of_rooms = int(adults_children_rooms[2].text) # rooms

        increment_button = self.find_elements(By.XPATH, '//button[@class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a"]')
        decrement_button = self.find_elements(By.XPATH, '//button[@class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 e91c91fa93"]')


        if const.ADULTS > num_of_adults:
            while num_of_adults < const.ADULTS:
                increment_button[0].click()
                num_of_adults += 1
        elif const.ADULTS < num_of_adults:
            while num_of_adults > const.ADULTS:
                decrement_button[0].click()
            num_of_adults -= 1
    
        if const.CHILDREN > num_of_children: 
            while num_of_children < const.CHILDREN:
                increment_button[1].click()
                children_age = self.find_element(By.XPATH, '//select[@class="ebf4591c8e"]').click()
                choose_age = self.find_element(By.XPATH , f'//select[@class="ebf4591c8e"]/option[text()="{const.CHILDREN_AGE} years old"]').click()
                num_of_children += 1

        if const.ROOMS > num_of_rooms:
            while num_of_rooms < const.ROOMS:
                increment_button[2].click()
                num_of_rooms += 1
        elif const.ROOMS < num_of_rooms:
            while num_of_rooms > const.ROOMS:
                decrement_button[2].click()
            num_of_rooms -= 1
     
    def searchButton(self):
        # Click the search button
        click_search = self.find_element(By.XPATH, '//button[@class="a83ed08757 c21c56c305 a4c1805887 f671049264 d2529514af c082d89982 cceeb8986b"]').click()

    def hotelLevelFiltering(self):
        # Filter hotels based on criteria
        try:
            very_good_rating_8_plus = self.find_element(By.XPATH, '//div[@data-filters-item="review_score:review_score=80"]//input[@value="review_score=80"]').click()
            hotels_with_3_starts = self.find_element(By.XPATH, '//div[@data-filters-item="class:class=3"]').click()
            hotels_with_4_starts = self.find_element(By.XPATH, '//div[@data-filters-item="class:class=4"]').click()
            hotels_with_5_starts = self.find_element(By.XPATH, '//div[@data-filters-item="class:class=5"]').click()
            free_cancellation_option = self.find_element(By.XPATH, '//div[@data-filters-item="fc:fc=2"]').click()
            hotels_only = self.find_element(By.CSS_SELECTOR, 'div[data-filters-item="popular:ht_id=204"].a53cbfa6de.ac9267e216.d8eb520c4e.ebc3dd5b38.bae4cd9be8.bf862b4098').click()

        except:
            pass

    def filterHotelDetails(self):
        collection = []

        while True:
            all_cards = self.find_element(By.CLASS_NAME, 'd4924c9e74')
            property_cards = all_cards.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

            for property in property_cards:
                try:    
                    hotel_name = property.find_element(By.CSS_SELECTOR, 'div[data-testid="title"].f6431b446c.a15b38c233').text
                    how_many_starts = property.find_element(By.CLASS_NAME, 'b3f3c831be').get_attribute('aria-label')
                    hotel_price = property.find_element(By.CLASS_NAME, 'f6431b446c.fbfd7c1165.e84eb96b1f').text
                    hotel_score = property.find_element(By.CLASS_NAME, 'a83ed08757.f88a5204c2.c057617e1a.b98133fb50').text.replace('\n', " ")
                    distance = property.find_element(By.CSS_SELECTOR, 'span[data-testid="distance"]').text
                    link = property.find_element(By.XPATH, '//a[@data-testid="availability-cta-btn"]').get_attribute('href')

                    # Create a dictionary for each property
                    property_data = {
                        "Hotel": hotel_name,
                        "Stars": how_many_starts,
                        "Price": hotel_price,
                        "Score": hotel_score,
                        "Distance" : distance,
                        "link": link
                    }

                    collection.append(property_data)

                except:
                    pass
   

            try:
                # Click the "Next page" button
                next_page = self.find_element(By.XPATH, '//button[@aria-label="Next page"]')
                if next_page.is_enabled():
                    next_page.click()
                else:
                    break  # Exit the loop when the "Next page" button is disabled
            except:
                break  # Exit the loop if the button is not found


        # Replace any character with an empty string - regular expression ( ant simble of money ₪/€/$)
        sorted_data = sorted(collection, key=lambda x: int(re.sub(r'[^\d]', '', x['Price']).replace(',', '').strip()))

        return sorted_data
        # for item in sorted_data[:const.LIMIT_SEARCH]:
        #     print(item)

    def filterPrice(self):
        self.refresh()
        left_btn = self.find_element(By.XPATH, '//div[@style="left: 0%;"]') 
        right_btn = self.find_element(By.XPATH, '//div[@class="d819a91462" and contains(@style, "right")]')

        # max_price = 500
        slider_width = right_btn.size['width']
        maximum_possible_price_str  = self.find_element(By.XPATH, "//input[@class='aabf012b69']").get_attribute('max')
        maximum_possible_price = int(maximum_possible_price_str)
        slider_offset = -100 - float(((const.MAX_PRICE / maximum_possible_price) * 100)) * (-1) 

        ActionChains(self).drag_and_drop_by_offset(left_btn, 0, 0).perform()
        ActionChains(self).drag_and_drop_by_offset(right_btn, slider_offset, 0).perform()

    def writeToExcel(self, sorted_data):
        # Convert sorted_data into a list of dictionaries using dictionary unpacking
        list_of_dicts = [{key: item[key] for key in ('Hotel', 'Stars', 'Price', 'Score', 'Distance', 'link')} for item in sorted_data]

        # Create a DataFrame from the data
        df = pd.DataFrame(list_of_dicts)

        # Define the Excel file name
        excel_file = "hotel_data.xlsx"

        # Write only the first LIMIT_SEARCH rows of the DataFrame to an Excel file
        df.head(const.LIMIT_SEARCH).to_excel(excel_file, index=False)  # Set index=False to exclude the index column