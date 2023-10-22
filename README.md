
<h1 align="center">BookingBot</h1>

<p align="center">
  <b>An Automated Hotel Booking Tool for Booking.com</b>
</p>


---

## Description

BookingBot is a Python-based automated tool designed to simplify and streamline the hotel booking process on Booking.com. This web scraper automates various tasks, including searching for hotels, applying filters, and sorting results based on your preferences. By the end of the process, you'll have neatly organized data to help you make the best choice for your stay.

---

## Installation

**1. Clone the Repository:**

```bash
git clone https://github.com/Stas-Fridman/bookingbot.git
```

**2. Set Up the Configuration:**

Navigate to the project folder and update the `constants.py` file with your preferences, such as destination, check-in/out dates, currency, and more.

**3. Install Dependencies:**

While in the project folder, install the required libraries:

```bash
pip install -r requirements.txt
```

Please note that you'll also need to install the `openpyxl` library for Excel file handling:

```bash
pip install openpyxl
```

**4. Web Driver Setup:**

Download the appropriate web driver for your browser and platform. Make sure the driver is in your system's PATH or specify its location in the code.

**5. Run the Bot:**

Execute the `run_hotels.py` script from outside the project folder to start BookingBot.

```bash
python path_to_project/run_hotels.py
```

---

## Usage

1. BookingBot will automate the process, scraping hotel data based on your preferences.
2. The results will be displayed and saved in an Excel file.

---

## Technologies Used

BookingBot is built with the following technologies and libraries:

- Python
- Selenium
- Pandas

---

## How to Use

1. Customize your search preferences in the `constants.py` file.
2. Execute `run_hotels.py` from outside the project folder to start the scraper.
3. Review the scraped data to make informed booking decisions.

---

## Contributing

We welcome contributions! If you'd like to improve BookingBot, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

<p align="center">
  Happy booking with BookingBot!
</p>
