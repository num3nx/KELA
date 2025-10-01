from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-default-browser-check")


driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()


CHROMEDRIVER_PATH = "/usr/bin/chromedriver"
URL = "https://www.google.com"
EXPECTED_STRING= "google"
OUTPUT_FILENAME = "URL_validation.txt"
driver.get(URL)

# assert ASSERT_URL in driver.current_url, f"Current URL is {driver.current_url}, and expected {ASSERT_URL}"

if EXPECTED_STRING in URL:
    print(f"OK, Current URL is {URL}, same as expected")
    with open(OUTPUT_FILENAME, "w") as file:
        file.write(driver.current_url)
else:
    print(f"Error, Current URL is {driver.current_url}, and not contain expected string: {EXPECTED_STRING}")

