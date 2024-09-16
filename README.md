# Canva Bulk Automation

This repository automates the process of creating designs in bulk using Canva. By leveraging **Selenium** for web automation and **Pandas** for handling Excel files, this tool allows you to input data from an Excel sheet and automatically populate Canva templates.

## Features
- Automates design creation in Canva with bulk data from Excel files.
- Uses Selenium for web browser automation.
- Easily customizable to suit different Canva templates by modifying XPath and CSS selectors.

## Requirements

- Python 3.x
- [Selenium](https://www.selenium.dev/)
- Web Driver (ChromeDriver, GeckoDriver, etc.) for your preferred browser
- Pandas

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/canva-bulk-automation.git
   cd canva-bulk-automation
   ```

2. **Install the required libraries:**
   ```bash
   pip install selenium pandas
   ```

3. **Download and Install WebDriver:**
   - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for Google Chrome.
   - [GeckoDriver](https://github.com/mozilla/geckodriver/releases) for Firefox.

   After downloading, place the driver in your system's PATH or specify its location in the script.


## Customization

- **Changing Excel columns:** If your Excel file has different column names, update the column names in `excel.py`.
- **Adjusting Canva element selectors:** XPath and CSS selectors for Canva elements may vary. Ensure to inspect the elements in the browser and modify the values in `main.py` accordingly.

## Disclaimer

This script is provided as-is, and Canva’s terms of service should be respected. This tool is not affiliated with or endorsed by Canva.

