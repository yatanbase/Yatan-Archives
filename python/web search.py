from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
import time

def search_and_print(driver, search_term):
    search_box = driver.find_element("name", "q")
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for the page to load
    print(f"Title after searching for '{search_term}': {driver.title}")

def main():
    # Path to Microsoft Edge WebDriver executable
    edge_driver_path = r'C:\Users\DELL\Downloads\msedgedriver.exe'  # Use a raw string

    # Create a Service instance with the path to the Edge WebDriver executable
    edge_service = EdgeService(executable_path=edge_driver_path)

    # Create a new instance of the Edge driver using the Service instance
    driver = webdriver.Edge(service=edge_service)

    # Open Edge browser and navigate to Google
    driver.get("https://www.bing.com")

    # Perform searches for ball 1 to ball 30

    search_term = f"ball "
    search_and_print(driver, search_term)

    search_term = f"asfdklj "
    search_and_print(driver, search_term)
    search_term = f"zxcv "
    search_and_print(driver, search_term)
    search_term = f"sdfwe "
    search_and_print(driver, search_term)

    # Close the browser window
   

if __name__ == "__main__":
    main()